from typing import List, Dict, Any, LiteralString
import gspread
from gsheetdb.worksheet import WorksheetWithSchema

class Database:
    def __init__(self, spreadsheet: gspread.Spreadsheet):
        """Initialize a database abstraction over a Google Spreadsheet."""
        self.spreadsheet = spreadsheet

    def get_collection(
        self, worksheet_name: LiteralString, schema: Dict[str, Any]
    ) -> WorksheetWithSchema:
        """Return a WorksheetWithSchema object."""
        try:
            worksheet = self.spreadsheet.worksheet(worksheet_name)
            headers = worksheet.row_values(1) 
            return WorksheetWithSchema(worksheet, schema=schema, headers=headers)
        except gspread.WorksheetNotFound:
            raise ValueError(f"Worksheet '{worksheet_name}' not found.")

    def create_collection(self, name: LiteralString, rows=1000, cols=26) -> WorksheetWithSchema:
        """Create a new worksheet."""
        worksheet = self.spreadsheet.add_worksheet(title=name, rows=rows, cols=cols)
        return WorksheetWithSchema(worksheet, schema={}, expected_headers=None)

    def drop_collection(self, worksheet_name: LiteralString) -> None:
        """Delete a worksheet."""
        worksheet = self.spreadsheet.worksheet(worksheet_name)
        self.spreadsheet.del_worksheet(worksheet)

    def list_collections(self):
        """List all worksheets with their row counts."""
        return {ws.title: ws.row_count for ws in self.spreadsheet.worksheets()}
