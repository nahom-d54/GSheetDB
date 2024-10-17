import unittest
from unittest.mock import MagicMock
from gsheetdb.worksheet import Worksheet

class TestWorksheet(unittest.TestCase):
    def setUp(self):
        self.mock_worksheet = MagicMock()
        self.collection = Worksheet(self.mock_worksheet)

    def test_insert_one(self):
        self.collection.insert_one({"name": "Alice", "age": 25})
        self.mock_worksheet.append_row.assert_called_once_with(["Alice", 25])

    def test_find_one(self):
        self.mock_worksheet.get_all_records.return_value = [{"name": "Alice", "age": 25}]
        result = self.collection.find_one({"name": "Alice"})
        self.assertEqual(result, {"name": "Alice", "age": 25})

if __name__ == "__main__":
    unittest.main()
