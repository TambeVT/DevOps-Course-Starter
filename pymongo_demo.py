import pymongo
import dotenv
import os

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_DB_CONNECTION_STRING"))

db = client.todoappdatabase

collection = db.todo_items

print(collection)

print(client.list_database_names())


# Insert a document into the database
collection.insert_one({"name": "A pymongo todo", "status": "To Do"})

# Read the documents from the DB into a Python list
documents = list(collection.find())

document = documents[0]

# Update a document
collection.update_one({"_id": document["_id"]}, {"$set": {"status": "Done"}})


# Read the documents from the DB into a Python list
documents = list(collection.find())

print(documents)