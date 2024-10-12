from domain.item import Item
from bson import ObjectId  

class ItemRepository():

    def __init__(self, mongo_client):
        self.mongo_client = mongo_client
        self.collection_name = "items"
        self.collection = mongo_client[self.collection_name]

    def insert_item(self, item):

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
        return item_id

    def find_all_items(self):
        items = self.collection.find()
        item_objects = []

        for item_data in items:
            item = Item(
                id=str(item_data.get("_id")),
                name=item_data.get("name"),
                category=item_data.get("category"),
                color=item_data.get("color"),
                style=item_data.get("style"),
                brand=item_data.get("brand"),
                season=item_data.get("season"),
                image_url=item_data.get("image_url")  
            )
            item_objects.append(item)
        return item_objects
    
    def delete_one_item(self, id):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return  result.deleted_count >= 1 

    def update_one_item(self, id: str, item_update: dict):

        result = self.collection.update_one(
            {"_id": ObjectId(id)}, 
            {"$set": item_update}  
        )
        return result

    def get_one_item_by_id(self, id):
        item = self.collection.find_one({"_id": ObjectId(id)})
        return item

    