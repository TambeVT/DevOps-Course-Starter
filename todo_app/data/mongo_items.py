from bson import objectID
import pymongo
import os

from todo_app.data.item import Item

def get_collection():
    client = pymongo.MongoClient(os.getenv("MONGO_DB_CONNECTION_STRING"))

    db = client[os.getenv("MONGODB_DATABASE_NAME")]

    collection = db[os.getenv("MONGODB_COLLECTION_NAME")]
    return collection


def add_item(new_todo_title: str):
    collection =get_collection(

    )
    new_item ={
        "name": new_todo_title,
        "status": "To Do"
    }

    collection.insert_one(new_item)
    

def get_items():
    collection = get_collection()
    mongodb_documents = list(collection.find())

    items = []

for document in mongodb_documents:
    item = Item.from_mongo_document(document)
    items.append(item)

    return items


def move_item_to_done(todo_id: str):
    collection.update_one({"_id": objectId["todo_id"]}, {"$set": {"status": "Done"}})

    