import pytest
from pymongo import MongoClient
from testcontainers.mongodb import MongoDbContainer



@pytest.fixture(scope="module")
def mongodb_container():
    with MongoDbContainer("mongo:latest") as mongo:
        yield  mongo.get_connection_url()

def test_mongodb_connection(mongodb_container):
    print(mongodb_container)
    client = MongoClient(mongodb_container)
    db = client["wardrobe_db"]
    collection = db["items"]

    item_dict = {
        "name": "tshirt blue",
        "category": "shirts",
        "color": "blue",
        "style": "sportive",
        "brand": "nike",
        "season": "2025",
        "image_url": "/urls.png"
    }

    insert_result = collection.insert_one(item_dict)

    assert insert_result.inserted_id is not None

    retrieved_document = collection.find_one({"name":  "tshirt blue"})
    assert retrieved_document is not None
