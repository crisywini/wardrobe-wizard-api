from fastapi import APIRouter
from domain.outfit import Outfit
from repository.outfit_repository import OutfitRepository
from service.outfit_service import OutfitService


from pymongo import MongoClient

router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["wardrobe_db"]

outfit_repository = OutfitRepository(db)
outfit_service = OutfitService(outfit_repository)

@router.get("/outfits")
def get_outfits():
    return outfit_service.get_all()

@router.post("/outfits")
def create_outfit(outfit: Outfit):
    print(outfit)
    return outfit_service.save(outfit)