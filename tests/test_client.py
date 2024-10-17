import unittest
from unittest.mock import MagicMock
from gsheetdb.client import GSheetClient

class TestGSheetClient(unittest.TestCase):
    def setUp(self):
        self.client = GSheetClient("path/to/credentials.json")
        self.mock_db = MagicMock()
        self.client.get_database = MagicMock(return_value=self.mock_db)

    def test_get_database(self):
        db = self.client.get_database("TestSheet")
        self.assertIsNotNone(db)
        self.client.get_database.assert_called_with("TestSheet")

if __name__ == "__main__":
    unittest.main()
