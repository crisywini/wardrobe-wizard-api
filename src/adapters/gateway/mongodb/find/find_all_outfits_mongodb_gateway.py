from pymongo.synchronous.database import Database

from src.adapters.gateway.mongodb.find.mapper.outfit_mongodb_mapper import map_to_entity
from src.ports.gateways.find.find_all_outfits_gateway import FindAllOutfitsGateway


class FindAllOutfitsMongoDBGateway(FindAllOutfitsGateway):
    def __init__(self, mongo_client: Database):
        self.mongo_client = mongo_client
        self.collection_name = "outfits"
        self.collection = mongo_client[self.collection_name]

    def run(self):
        outfits_mongodb = self.collection.find()
        return list(map(map_to_entity, outfits_mongodb))
