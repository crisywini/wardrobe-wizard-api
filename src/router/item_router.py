from fastapi import APIRouter, UploadFile, Form, File
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
async def create_item(file: UploadFile = File(...), item: str = Form(...)):

    file_location = f"static/images/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    item_data = Item.parse_raw(item)
    item_data.image_url = f"/images/{file.filename}"
    
    data = item_repository.insert_item(item_data)

    return str(data)