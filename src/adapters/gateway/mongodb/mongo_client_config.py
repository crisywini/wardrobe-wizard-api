from pymongo import MongoClient
import os

client = None
mongo_db_instance = None

def get_mongodb_client():
    global client
    if client is None:
        mongo_url = os.getenv("MONGO_URL", "mongodb://mongo:27017/wardrobe_db")
        client = MongoClient(mongo_url)
    return client

def get_mongodb_instance():
    global mongo_db_instance
    if mongo_db_instance is None:
        mongo_db_instance = get_mongodb_client()["wardrobe_db"]
    return mongo_db_instance