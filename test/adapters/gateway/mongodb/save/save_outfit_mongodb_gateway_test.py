import pytest
from pymongo import MongoClient
from testcontainers.mongodb import MongoDbContainer

from src.adapters.gateway.mongodb.save.save_item_mongdb_gateway import SaveItemMongoDBGateway
from src.adapters.gateway.mongodb.save.save_outfit_mongodb_gateway import SaveOutfitMongoDBGateway
from src.domain.builders.item_builder import ItemBuilder
from src.domain.builders.outfit_builder import OutfitBuilder


@pytest.fixture(scope="module")
def mongodb_container():
    with MongoDbContainer("mongo:latest") as mongo:
        yield mongo.get_connection_url()


def test_register_outfit_happy_path(mongodb_container):
    client = MongoClient(mongodb_container)
    db = client["wardrobe_db"]
    collection = db["outfits"]
    gateway = SaveOutfitMongoDBGateway(db)

    shirt, pants, shoes = setup_happy_path(db)

    outfit = OutfitBuilder().set_name("Cool Gym outfit").set_category("gym").set_items([shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()
    outfit_saved = gateway.run(outfit)

    assert outfit_saved.id is not None

    retrieved_document = collection.find_one({"name": "Cool Gym outfit"})
    assert retrieved_document is not None


def setup_happy_path(db):
    gateway = SaveItemMongoDBGateway(db)

    shirt = ItemBuilder().set_name("tshirt blue").set_category("shirts").set_color("blue").set_style(
        "sportive").set_brand("nike").set_season("2025").set_image_url("/image_url.jpeg").build()
    pants = ItemBuilder().set_name("pants blue").set_category("pants").set_color("blue").set_style(
        "sportive").set_brand("nike").set_season("2025").set_image_url("/image_url.jpeg").build()
    shoes = ItemBuilder().set_name("shoes blue").set_category("shoes").set_color("blue").set_style(
        "sportive").set_brand("nike").set_season("2025").set_image_url("/image_url.jpeg").build()

    shirt_saved = gateway.run(shirt)
    pants_saved = gateway.run(pants)
    shoes_saved = gateway.run(shoes)
    return shirt_saved, pants_saved, shoes_saved