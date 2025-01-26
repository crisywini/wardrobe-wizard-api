from pymongo import MongoClient
from bson import ObjectId

from src.domain.builders.item_builder import ItemBuilder
from src.domain.builders.outfit_builder import OutfitBuilder
from src.ports.gateways.find.find_outfit_by_id_gateway import FindOutfitByIdGateway


class FindOutfitByIdMongoDBGateway(FindOutfitByIdGateway):
    def __init__(self, mongo_client: MongoClient):
        self.mongo_client = mongo_client
        self.collection_name = "outfits"
        self.collection = mongo_client[self.collection_name]

    def run(self, id: str):
        outfit = self.collection.find_one({"_id": ObjectId(id)})
        if outfit:
            id_mongo = str(outfit.get("_id"))
            name = outfit.get("name")
            category = outfit.get("category")
            items = []
            for item in outfit["items"]:
                items.append(self._build_item(item))
            return OutfitBuilder.set_id(id_mongo).set_name(name).set_category(category).set_items(items)
        else:
            return None

    def _build_item(self, item):
        id_mongo = str(item.get("_id"))
        name = item.get("name")
        category = item.get("category")
        color = item.get("color")
        style = item.get("style")
        brand = item.get("brand")
        season = item.get("season")
        image_url = item.get("image_url")
        return ItemBuilder.set_id(id_mongo).set_name(name).set_category(category).set_color(
            color).set_style(style).set_brand(brand).set_season(season).set_image_url(
            image_url).build()
