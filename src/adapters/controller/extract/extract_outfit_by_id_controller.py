from fastapi import APIRouter

from src.adapters.gateway.mongodb.find.find_outfit_by_id_mongodb_gateway import FindOutfitByIdMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.find.find_outfit_by_id_use_case import FindOutfitByIdUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

find_outfit_by_id_mongodb_gateway = FindOutfitByIdMongoDBGateway(mongodb_instance)
find_outfit_by_id_use_case = FindOutfitByIdUseCase(find_outfit_by_id_mongodb_gateway)


@router.get(path="/outfits/{outfit_id}")
def get_outfit_by_id(outfit_id: str):
    return find_outfit_by_id_use_case.run(outfit_id)