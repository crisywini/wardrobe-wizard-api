import pytest
from PIL.ImageChops import constant
from pymongo import MongoClient
from testcontainers.mongodb import MongoDbContainer

import src.adapters.controller.config.constants as constant
from src.adapters.gateway.mongodb.save.save_item_mongdb_gateway import SaveItemMongoDBGateway
from src.adapters.gateway.mongodb.save.save_outfit_mongodb_gateway import SaveOutfitMongoDBGateway
from src.domain.builders.item_builder import ItemBuilder
from src.domain.builders.outfit_builder import OutfitBuilder
from src.use_cases.save.save_outfit_use_case import SaveOutfitUseCase

import os


@pytest.fixture(scope="module")
def mongodb_container():
    with MongoDbContainer("mongo:latest") as mongo:
        yield mongo.get_connection_url()


def test_save_outfit_with_correct_items_will_create_default_image(mongodb_container):
    constant.UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "../../resources")
    client = MongoClient(mongodb_container)
    db = client["wardrobe_db"]
    gateway = SaveOutfitMongoDBGateway(db)
    use_case = SaveOutfitUseCase(gateway)

    shirt, pants, shoes = save_items(db)

    outfit = OutfitBuilder().set_name("Cool American outfit").set_category("gym").set_items(
        [shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()
    saved_outfit = use_case.run(outfit)

    assert saved_outfit is not None


def save_items(db):
    gateway = SaveItemMongoDBGateway(db)

    shirt = ItemBuilder().set_name("Green true shirt").set_category("shirts").set_color("green").set_style(
        "sportive").set_brand("True").set_season("2024").set_image_url(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/true_shirt.png"))).build()
    pants = ItemBuilder().set_name("Blue jeans").set_category("pants").set_color("blue").set_style(
        "Jeans").set_brand("nike").set_season("2024").set_image_url(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/jeans_koaj.png"))).build()
    shoes = ItemBuilder().set_name("white shoes").set_category("shoes").set_color("white").set_style(
        "sportive").set_brand("new balance").set_season("2024").set_image_url(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/new_balance_shoes.png"))).build()

    shirt_saved = gateway.run(shirt)
    pants_saved = gateway.run(pants)
    shoes_saved = gateway.run(shoes)
    return shirt_saved, pants_saved, shoes_saved
