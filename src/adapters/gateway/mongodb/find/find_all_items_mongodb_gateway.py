from pymongo.synchronous.database import Database

from src.domain.builders.item_builder import ItemBuilder
from src.ports.gateways.find.find_all_items_gateway import FindAllItemsGateway


class FindAllItemsMongoDBGateway(FindAllItemsGateway):
    def __init__(self, mongo_client: Database):
        self.mongo_client = mongo_client
        self.collection_name = "items"
        self.collection = mongo_client[self.collection_name]

    def run(self):
        items_mongodb = self.collection.find()
        return list(map(self._build_item, items_mongodb))

    def _build_item(self, item):
        builder = ItemBuilder().set_id(item.get("_id")).set_name(item.get("name")).set_category(
            item.get("category")).set_color(item.get("color")).set_style(item.get("style")).set_brand(
            item.get("brand")).set_season(item.get("season")).set_image_url(item.get("image_url"))
        return builder.build()
