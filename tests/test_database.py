import unittest
from unittest.mock import MagicMock
from gsheetdb.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.spreadsheet = MagicMock()
        self.database = Database(self.spreadsheet)

    def test_get_collection(self):
        self.spreadsheet.worksheet.return_value = MagicMock()
        collection = self.database.get_collection("Sheet1")
        self.assertIsNotNone(collection)

    def test_list_collections(self):
        self.spreadsheet.worksheets.return_value = [MagicMock(title="Sheet1", row_count=10)]
        result = self.database.list_collections()
        self.assertEqual(result, {"Sheet1": 10})

if __name__ == "__main__":
    unittest.main()
