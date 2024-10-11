from fastapi import APIRouter
from domain.item import Item
from repository.item_repository  import ItemRepository
from pymongo import MongoClient
from bson import ObjectId

router = APIRouter()
client = MongoClient("mongodb://localhost:27017/")
db = client["wardrobe_db"]

item_repository = ItemRepository(db)

@router.get("/items/")
def get_items():
    return item_repository.find_all_items()

@router.post("/items/")
def create_item(item: Item):
    return {"message": f"Item {item.name} creado exitosamente"}
