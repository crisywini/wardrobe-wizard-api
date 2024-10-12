from fastapi import APIRouter
from domain.outfit import Outfit

router = APIRouter()

@router.get("/outfits/")
def get_outfits():
    return {"outfits": ["outfit1", "outfit2"]}

@router.post("/outfits/")
def create_outfit(outfit: Outfit):
    return {"message": f"Outfit {outfit.name} creado exitosamente"}
