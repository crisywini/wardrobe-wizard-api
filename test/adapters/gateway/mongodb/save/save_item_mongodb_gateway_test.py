import pytest
from pymongo import MongoClient
from testcontainers.mongodb import MongoDbContainer

from src.adapters.gateway.mongodb.save.save_item_mongdb_gateway import SaveItemMongoDBGateway
from src.domain.builders.item_builder import ItemBuilder


@pytest.fixture(scope="module")
def mongodb_container():
    with MongoDbContainer("mongo:latest") as mongo:
        yield mongo.get_connection_url()


def test_mongodb_connection(mongodb_container):
    print(mongodb_container)
    client = MongoClient(mongodb_container)
    db = client["wardrobe_db"]
    collection = db["items"]
    gateway = SaveItemMongoDBGateway(db)

    item = ItemBuilder().set_name("tshirt blue").set_category("shirts").set_color("blue").set_style(
        "sportive").set_brand("nike").set_season("2025").set_image_url("/image_url.jpeg").build()

    item_saved = gateway.run(item)

    assert item_saved.id is not None

    retrieved_document = collection.find_one({"name": "tshirt blue"})
    assert retrieved_document is not None
