from pymongo import MongoClient

from src.domain.builders.item_builder import ItemBuilder
from src.domain.entities.item import Item
from src.ports.gateways.save.save_item_gateway import SaveItemGateway


class SaveItemMongoDBGateway(SaveItemGateway):
    def __init__(self, mongo_client: MongoClient):
        self.mongo_client = mongo_client
        self.collection_name = "items"
        self.collection = mongo_client[self.collection_name]

    def run(self, item: Item):
        item_dict = {
            "name": item.name,
            "category": item.category,
            "color": item.color,
            "style": item.style,
            "brand": item.brand,
            "season": item.season,
            "image_url": item.image_url
        }
        item_id = self.collection.insert_one(item_dict).inserted_id
        return ItemBuilder.set_id(item_id).set_name(item.name).set_category(item.category).set_color(
            item.color).set_style(item.style).set_brand(item.brand).set_season(item.season).set_image_url(
            item.image_url).build()
