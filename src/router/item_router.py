from fastapi import APIRouter
from domain.item import Item

router = APIRouter()

@router.get("/items/")
def get_items():
    return {"items": ["item1", "item2", "item3"]}

@router.post("/items/")
def create_item(item: Item):
    return {"message": f"Item {item.name} creado exitosamente"}
