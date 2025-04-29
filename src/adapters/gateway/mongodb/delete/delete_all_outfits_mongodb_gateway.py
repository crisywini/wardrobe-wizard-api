from pymongo.synchronous.database import Database

from src.ports.gateways.delete.delete_all_outfits_gateway import DeleteAllOutfitsGateway


class DeleteAllOutfitsMongoDBGateway(DeleteAllOutfitsGateway):

    def __init__(self, mongo_client: Database):
        self.mongo_client = mongo_client
        self.collection_name = "outfits"
        self.collection = mongo_client[self.collection_name]

    def run(self):
        return self.collection.delete_many({}).deleted_count 