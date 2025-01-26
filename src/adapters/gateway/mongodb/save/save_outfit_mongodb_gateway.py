from bson import ObjectId
from pymongo.synchronous.database import Database

from src.domain.builders.outfit_builder import OutfitBuilder
from src.domain.entities.outfit import Outfit
from src.ports.gateways.save.save_outfit_gateway import SaveOutfitGateway

class SaveOutfitMongoDBGateway(SaveOutfitGateway):
    def __init__(self, mongo_client: Database):
        self.mongo_client = mongo_client
        self.collection_name = "outfits"
        self.collection = mongo_client[self.collection_name]

    def run(self, outfit: Outfit):
        outfit_dict = {
            "name": outfit.name,
            "category": outfit.category,
            "items": outfit.items
        }
        outfit_id = self.collection.insert_one(outfit_dict).inserted_id
        return OutfitBuilder().set_id(outfit_id).set_name(outfit.name).set_items(outfit.items).set_category(
            outfit.category)
