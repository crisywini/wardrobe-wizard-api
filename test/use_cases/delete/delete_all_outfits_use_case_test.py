import os

import pytest
from pymongo import MongoClient
from testcontainers.mongodb import MongoDbContainer
import src.adapters.controller.config.constants as constant

from src.adapters.gateway.mongodb.delete.delete_all_outfits_mongodb_gateway import DeleteAllOutfitsMongoDBGateway
from src.adapters.gateway.mongodb.find.find_all_outfits_mongodb_gateway import FindAllOutfitsMongoDBGateway
from src.adapters.gateway.mongodb.save.save_item_mongdb_gateway import SaveItemMongoDBGateway
from src.adapters.gateway.mongodb.save.save_outfit_mongodb_gateway import SaveOutfitMongoDBGateway
from src.domain.builders.item_builder import ItemBuilder
from src.domain.builders.outfit_builder import OutfitBuilder
from src.use_cases.delete.delete_all_outfits_use_case import DeleteAllOutfitsUseCase
from src.use_cases.find.find_all_outfits_use_case import FindAllOutfitsUseCase
from src.use_cases.save.save_outfit_use_case import SaveOutfitUseCase


@pytest.fixture(scope="module")
def mongodb_container():
    with MongoDbContainer("mongo:latest") as mongo:
        yield mongo.get_connection_url()


def test_delete_all_outfits(mongodb_container):
    client = MongoClient(mongodb_container)
    db = client["wardrobe_db"]
    save_outfits(db)

    gateway = DeleteAllOutfitsMongoDBGateway(db)
    use_case = DeleteAllOutfitsUseCase(gateway)

    get_all_outfits_gateway = FindAllOutfitsMongoDBGateway(db)
    get_all_outfits_use_case = FindAllOutfitsUseCase(get_all_outfits_gateway)

    response = use_case.run()
    response_all_outfits = get_all_outfits_use_case.run()
    assert response == 3
    assert len(response_all_outfits) == 0

def save_outfits(db):
    constant.UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "../../resources")

    gateway = SaveOutfitMongoDBGateway(db)
    use_case = SaveOutfitUseCase(gateway)

    shirt, pants, shoes = save_items(db)

    outfit = OutfitBuilder().set_name("Cool American outfit").set_category("gym").set_items(
        [shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()
    outfit2 = OutfitBuilder().set_name("Cool American outfit2").set_category("gym").set_items(
        [shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()
    outfit3 = OutfitBuilder().set_name("Cool American outfit3").set_category("gym").set_items(
        [shirt.to_dict(), pants.to_dict(), shoes.to_dict()]).build()

    use_case.run(outfit)
    use_case.run(outfit2)
    use_case.run(outfit3)

def save_items(db):
    gateway = SaveItemMongoDBGateway(db)

    shirt = ItemBuilder().set_name("Green true shirt").set_category("shirts").set_color("green").set_style(
        "sportive").set_brand("True").set_season("2024").set_image_url(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/true_shirt.png"))).build()
    pants = ItemBuilder().set_name("Coffee jeans").set_category("pants").set_color("blue").set_style(
        "Jeans").set_brand("koaj").set_season("2024").set_image_url(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/coffee_pants.jpg"))).build()
    shoes = ItemBuilder().set_name("white shoes").set_category("shoes").set_color("white").set_style(
        "sportive").set_brand("new balance").set_season("2024").set_image_url(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/new_balance_shoes.png"))).build()

    shirt_saved = gateway.run(shirt)
    pants_saved = gateway.run(pants)
    shoes_saved = gateway.run(shoes)
    return shirt_saved, pants_saved, shoes_saved