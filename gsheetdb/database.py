from gsheetdb.worksheet import Worksheet
import gspread

class Database:
    def __init__(self, spreadsheet: gspread.Spreadsheet):
        """Initialize a database abstraction over a Google Spreadsheet."""
        self.spreadsheet = spreadsheet

    def get_collection(self, worksheet_name: str) -> Worksheet:
        """Return a Worksheet (Collection) object."""
        try:
            worksheet = self.spreadsheet.worksheet(worksheet_name)
            return Worksheet(worksheet)
        except gspread.WorksheetNotFound:
            raise ValueError(f"Worksheet '{worksheet_name}' not found.")

    def create_collection(self, name: str, rows=1000, cols=26) -> Worksheet:
        """Create a new worksheet."""
        worksheet = self.spreadsheet.add_worksheet(title=name, rows=rows, cols=cols)
        return Worksheet(worksheet)

    def drop_collection(self, worksheet_name: str) -> None:
        """Delete a worksheet."""
        worksheet = self.spreadsheet.worksheet(worksheet_name)
        self.spreadsheet.del_worksheet(worksheet)

    def list_collections(self):
        """List all worksheets with their row counts."""
        return {ws.title: ws.row_count for ws in self.spreadsheet.worksheets()}
