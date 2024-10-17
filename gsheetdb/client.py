import gspread
from google.oauth2.service_account import Credentials
from gsheetdb.database import Database

class GSheetClient:
    def __init__(self, creds_path: str, scopes=None):
        """Initialize the Google Sheets client."""
        if scopes is None:
            scopes = ["https://www.googleapis.com/auth/spreadsheets",
                      "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
        self.client = gspread.authorize(creds)


    def get_database(self, sheet_name: str) -> Database:
        """Return a Database object representing a Google Spreadsheet."""
        spreadsheet = self.client.open(sheet_name)
        return Database(spreadsheet)
