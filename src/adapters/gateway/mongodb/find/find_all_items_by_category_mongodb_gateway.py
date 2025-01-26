from pymongo.synchronous.database import Database

from src.adapters.gateway.mongodb.find.mapper.item_mongodb_mapper import map_to_entity
from src.ports.gateways.find.find_all_items_by_category_gateway import FindAllItemsByCategoryGateway


class FindAllItemsByCategoryMongoDBGateway(FindAllItemsByCategoryGateway):
    def __init__(self, mongo_client: Database):
        self.mongo_client = mongo_client
        self.collection_name = "items"
        self.collection = mongo_client[self.collection_name]

    def run(self, category: str):
        items = self.collection.find({
            "category": category
        })
        return list(map(map_to_entity, items))


