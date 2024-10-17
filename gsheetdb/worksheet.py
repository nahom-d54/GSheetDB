from typing import List, Dict, Optional, Any
from gsheetdb.query import apply_filters

class Worksheet:
    def __init__(self, worksheet):
        """Initialize with a worksheet object."""
        self.worksheet = worksheet
        self.index_cache = {}

    def create_index(self, column_name: str):
        """Create an index for fast lookups."""
        records = self.worksheet.get_all_records()
        self.index_cache[column_name] = {row[column_name]: row for row in records}

    def find_by_index(self, column_name: str, value: Any) -> Optional[Dict]:
        """Find a row using the index."""
        if column_name not in self.index_cache:
            self.create_index(column_name)
        return self.index_cache[column_name].get(value)

    def find(self, filter_query: Dict = None) -> List[Dict]:
        """Find rows that match the query."""
        rows = self.worksheet.get_all_records()
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
        rows = self.worksheet.get_all_records()
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
