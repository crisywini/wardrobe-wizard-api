import pytest
from pymongo import MongoClient
from testcontainers.mongodb import MongoDbContainer

from src.adapters.gateway.mongodb.find.find_all_outfits_mongodb_gateway import FindAllOutfitsMongoDBGateway
from src.adapters.gateway.mongodb.save.save_item_mongdb_gateway import SaveItemMongoDBGateway
from src.adapters.gateway.mongodb.save.save_outfit_mongodb_gateway import SaveOutfitMongoDBGateway
from src.domain.builders.item_builder import ItemBuilder
from src.domain.builders.outfit_builder import OutfitBuilder
from src.use_cases.find.find_all_outfit_categories_use_case import FindAllOutfitCategoriesUseCase


@pytest.fixture(scope="module")
def mongodb_container():
    with MongoDbContainer("mongo:latest") as mongo:
        yield mongo.get_connection_url()


def test_get_all_categories(mongodb_container):
    client = MongoClient(mongodb_container)
    db = client["wardrobe_db"]
    save_outfits(mongodb_container)
    gateway = FindAllOutfitsMongoDBGateway(db)
    use_case = FindAllOutfitCategoriesUseCase(gateway)

    categories = use_case.run()

    assert categories is not None
    assert len(categories) == 3
    assert categories == set(["gym", "streetwear", "casual"])


def save_outfits(mongodb_container):
    client = MongoClient(mongodb_container)
    db = client["wardrobe_db"]
    gateway = SaveOutfitMongoDBGateway(db)

    shirt, pants, shoes = save_items(db)

    outfit = OutfitBuilder().set_name("Cool Gym outfit").set_category("gym").set_items(
        [shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()
    gateway.run(outfit)

    outfit_2 = OutfitBuilder().set_name("Cool Streetwear outfit").set_category("streetwear").set_items(
        [shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()
    gateway.run(outfit_2)

    outfit_3 = OutfitBuilder().set_name("Cool Casual outfit").set_category("casual").set_items(
        [shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()
    gateway.run(outfit_3)


def save_items(db):
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