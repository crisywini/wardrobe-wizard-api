from pymongo.synchronous.database import Database

from src.domain.builders.outfit_builder import OutfitBuilder
from src.ports.gateways.find.find_all_outfits_gateway import FindAllOutfitsGateway


class FindAllOutfitsMongoDBGateway(FindAllOutfitsGateway):
    def __init__(self, mongo_client: Database):
        self.mongo_client = mongo_client
        self.collection_name = "outfits"
        self.collection = mongo_client[self.collection_name]

    def run(self):
        outfits_mongodb = self.collection.find()
        return list(
            map(lambda outfit: OutfitBuilder().set_id(outfit.get("id")).set_name(outfit.get("name")).set_category(
                outfit.get("category")).set_items(outfit.get("items")).build(), outfits_mongodb))

