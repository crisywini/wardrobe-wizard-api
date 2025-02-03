from bson import ObjectId
from pymongo.synchronous.database import Database

from src.domain.builders.item_builder import ItemBuilder
from src.ports.gateways.find.find_item_by_id_gateway import FindItemByIdGateway


class FindItemByIdMongoDBGateway(FindItemByIdGateway):

    def __init__(self, mongo_client: Database):
        self.mongo_client = mongo_client
        self.collection_name = "items"
        self.collection = mongo_client[self.collection_name]

    def run(self, id: str):
        item = self.collection.find_one({"_id": ObjectId(id)})

        if item:
            id_mongo = str(item.get("_id"))
            name = item.get("name")
            category = item.get("category")
            color = item.get("color")
            style = item.get("style")
            brand = item.get("brand")
            season = item.get("season")
            image_url = item.get("image_url")
            return ItemBuilder().set_id(id_mongo).set_name(name).set_category(category).set_color(
                color).set_style(style).set_brand(brand).set_season(season).set_image_url(
                image_url).build()
        else:
            return None
