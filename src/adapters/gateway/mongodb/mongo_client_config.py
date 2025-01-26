from pymongo import MongoClient

client = None
mongo_db_instance = None

def get_mongodb_client():
    global client
    if client is None:
        client = MongoClient("mongodb://localhost:27017/")
    return client

def get_mongodb_instance():
    global mongo_db_instance
    if mongo_db_instance is None:
        mongo_db_instance = get_mongodb_client()["wardrobe_db"]
    return mongo_db_instance