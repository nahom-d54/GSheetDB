from typing import List, Dict, Optional, Any
from gsheetdb.query import apply_filters
from gsheetdb.models import create_dynamic_model
from gsheetdb.utils import column_letter
from pydantic import ValidationError

class Worksheet:
    def __init__(self, worksheet):
        """Initialize with a worksheet object."""
        self.worksheet = worksheet
        self.index_cache = {}

    def get_all_records(self): 
        records = self.worksheet.get_all_records()
        return records
    
    def create_index(self, column_name: str):
        """Create an index for fast lookups."""
        records = self.get_all_records()
        self.index_cache[column_name] = {row[column_name]: row for row in records}

    def find_by_index(self, column_name: str, value: Any) -> Optional[Dict]:
        """Find a row using the index."""
        if column_name not in self.index_cache:
            self.create_index(column_name)
        return self.index_cache[column_name].get(value)

    def find(self, filter_query: Dict = None) -> List[Dict]:
        """Find rows that match the query."""
        rows = self.get_all_records()
        return apply_filters(rows, filter_query)

    def find_one(self, filter_query: Dict) -> Optional[Dict]:
        """Find the first matching row."""
        results = self.find(filter_query)
        return results[0] if results else None

    def insert_one(self, data: Dict):
        """Insert a single row."""
        self.worksheet.append_row(list(data.values()))

    def insert_many(self, data_list: List[Dict]):
        """Insert multiple rows."""
        values = [list(data.values()) for data in data_list]
        self.worksheet.append_rows(values)

    def update_one(self, filter_query: Dict, new_data: Dict) -> bool:
        """Update the first matching row."""
        rows = self.get_all_records()
        for i, row in enumerate(rows, start=2):
            if apply_filters([row], filter_query):
                self.worksheet.update(f"A{i}", [list(new_data.values())])
                return True
        return False

    def delete_one(self, filter_query: Dict) -> bool:
        """Delete the first matching row."""
        rows = self.worksheet.get_all_records()
        for i, row in enumerate(rows, start=2):
            if apply_filters([row], filter_query):
                self.worksheet.delete_rows(i)
                return True
        return False
    
class WorksheetWithSchema(Worksheet):
    def __init__(self, worksheet, schema: Dict[str, Any], headers: List = None):
        """Set a schema for the worksheet data."""
        super().__init__(worksheet)
        self.headers = headers
        self.schema_model = create_dynamic_model(schema)

    def insert_one(self, data: Dict):
        """Insert a single row with schema validation."""
        try:
            validated_data = self.schema_model.from_dict(data)  # Validate data against the schema
            self.worksheet.append_row(list(validated_data.dict().values()))
        except ValidationError as e:
            print(f"Data validation error: {e}")  # Handle validation errors

    def insert_many(self, data_list: List[Dict]):
        """Insert multiple rows with schema validation."""
        validated_data_list = []
        for data in data_list:
            try:
                validated_data = self.schema_model.from_dict(data)  # Validate each item
                validated_data_list.append(validated_data)
            except ValidationError as e:
                print(f"Data validation error for {data}: {e}")  # Handle validation errors
        
        values = [list(data.dict().values()) for data in validated_data_list]
        self.worksheet.append_rows(values)


    def query(self, query_string: str) -> List[Dict[str, Any]]:
        """Execute a SQL-like query using Google Sheets' QUERY function."""
        # Dynamically determine the range of the worksheet
        num_rows = self.worksheet.row_count
        num_cols = self.worksheet.col_count
        range_ref = f"A1:{column_letter(num_cols)}{num_rows}"  # Handle columns beyond Z

        # Construct the full QUERY function
        full_query = f'=QUERY({range_ref}, "{query_string}")'

        # Fetch query results
        query_results = self.worksheet.get_values()

        # Convert query results to dictionaries using expected headers
        if self.headers:
            return [dict(zip(self.headers, row)) for row in query_results[1:]]
        else:
            raise ValueError("Expected headers must be set to use this method.")

    def find(self, filter_query: Dict) -> List[Dict[str, Any]]:
        """Execute a MongoDB-like query using Google Sheets' QUERY function."""
        # Translate the MongoDB-like filter query to SQL-like syntax
        where_clause = self.translate_query(filter_query)

        # Construct the full SQL-like query
        query_string = f"SELECT * WHERE {where_clause}"

        # Call the query method with the constructed query string
        return self.query(query_string)

    def translate_query(self, filter_query: Dict) -> str:
        """Translate a MongoDB-like query to a SQL-like WHERE clause."""
        def parse_condition(key, condition):
            if isinstance(condition, dict):
                if "$eq" in condition:
                    return f"{key} = '{condition['$eq']}'"
                elif "$gt" in condition:
                    return f"{key} > {condition['$gt']}"
                elif "$lt" in condition:
                    return f"{key} < {condition['$lt']}"
                elif "$gte" in condition:
                    return f"{key} >= {condition['$gte']}"
                elif "$lte" in condition:
                    return f"{key} <= {condition['$lte']}"
                elif "$in" in condition:
                    values = ", ".join([f"'{v}'" for v in condition["$in"]])
                    return f"{key} IN ({values})"
            else:
                return f"{key} = '{condition}'"

        clauses = []

        if "$and" in filter_query:
            clauses = [self.translate_query(sub_query) for sub_query in filter_query["$and"]]
            return " AND ".join(clauses)

        if "$or" in filter_query:
            clauses = [self.translate_query(sub_query) for sub_query in filter_query["$or"]]
            return " OR ".join(clauses)

        for key, condition in filter_query.items():
            clauses.append(parse_condition(key, condition))

        return " AND ".join(clauses)


