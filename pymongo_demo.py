import pymongo
import dotenv
import os

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_DB_CONNECTION_STRING"))

db = client.todoappdatabase

collection = db.todo_items

print(collection)

print(client.list_database_names())