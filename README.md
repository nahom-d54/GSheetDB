# GSheetDB

`GSheetDB` is a **PyMongo-inspired** library that allows you to interact with **Google Sheets** like a database. It provides a Pythonic interface to manage worksheets, perform CRUD operations, and run advanced queries.

## **Features**

- **CRUD operations**: Insert, update, delete, and find rows.
- **Advanced queries**: Use MongoDB-style filters with `$gt`, `$in`, `$eq`, etc.
- **Batch operations**: Insert or update multiple rows efficiently.
- **Indexing**: Create indexes for fast lookups.
- **Cross-sheet joins**: Join data across worksheets.
- **CLI support**: Interact with Google Sheets via the command line.

## **Installation**

Install the library using `pip`:

```bash
pip install GSheetDB
```

## **Usage**
### 1. Authenticate with Google Sheets
Create a service account and download the credentials JSON. Initialize the client with your credentials:

``` python

from gsheetdb.client import GSheetClient

client = GSheetClient("path/to/credentials.json")
db = client.get_database("MySpreadsheet")
collection = db.get_collection("Sheet1")
```
### 2. Insert Data
```python
collection.insert_one({"name": "Alice", "age": 25})
collection.insert_many([
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
])
```
### 3. Query Data
``` python
# Find all users older than 25
results = collection.find({"age": {"$gt": 25}})
print(results)

# Find a specific user
user = collection.find_one({"name": "Alice"})
print(user)
```
### 4. Update Data
``` python 
collection.update_one({"name": "Alice"}, {"name": "Alice", "age": 26})
```
### 5. Delete Data
``` python
collection.delete_one({"name": "Charlie"})
```
## **CLI Usage**
You can also interact with Google Sheets using the command line:

``` bash
gsheetdb-cli find "MySpreadsheet" "Sheet1" '{"age": {"$gt": 25}}'
Testing
Run the test suite using:
```
``` bash
python -m unittest discover tests/
```
## **License**
This project is licensed under the MIT License.

## **Acknowledgments**

This project is a collaborative effort, developed with contributions from users and insights from the community. Special thanks to **Lexi**, an AI assistant developed by OpenAI, for assisting in the development and providing suggestions throughout the process.
