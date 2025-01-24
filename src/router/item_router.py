from fastapi import APIRouter, UploadFile, Form, File
from domain.item import Item
from repository.item_repository  import ItemRepository
from service.item_service  import ItemService

from pymongo import MongoClient

router = APIRouter()
client = MongoClient("mongodb://localhost:27017/")
db = client["wardrobe_db"]

item_repository = ItemRepository(db)
item_service = ItemService(item_repository)


@router.get("/items")
def get_items():
    return item_service.get_all()

@router.post("/items")
async def create_item(file: UploadFile = File(...), item: str = Form(...)):

    file_location = f"/Users/cristian.sanchezp/Documents/project/crisi-code-lab/personal/the-wardrobe-grimmerie/public/images/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    item_data = Item.parse_raw(item)
    item_data.image_url = f"/images/{file.filename}"
    
    id = item_service.save(item_data)

    return id

@router.get("/items/{item_id}")
def get_item(item_id: str):
    return item_service.get_by_id(item_id)

@router.delete("/items/{item_id}")
def delete_item(item_id: str):
    return item_service.delete_by_id(item_id)