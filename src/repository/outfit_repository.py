from domain.outfit import Outfit



class OutfitRepository():
    
    def __init__(self, mongo_client):
        self.mongo_client = mongo_client
        self.collection_name = "outfits"
        self.collection = mongo_client[self.collection_name]

    def insert_outfit(self, outfit: Outfit):
        return self.collection.insert_one(outfit.dict()).inserted_id
    
    def find_all_outfits(self):
        outfits = self.collection.find()
        outfit_objects = []
        
        for outfit_data in outfits:
            outfit = Outfit(name=outfit_data.get("name"), items=outfit_data.get("items"))
            outfit_objects.append(outfit)
        
        return outfit_objects