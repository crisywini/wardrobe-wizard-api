from fastapi import APIRouter

from src.adapters.gateway.mongodb.find.find_all_outfits_mongodb_gateway import FindAllOutfitsMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.find.find_all_outfits_use_case import FindAllOutfitsUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

find_all_outfits_mongodb_gateway = FindAllOutfitsMongoDBGateway(mongodb_instance)
find_all_outfits_use_case = FindAllOutfitsUseCase(find_all_outfits_mongodb_gateway)


@router.get(path="/outfits")
def get_all_outfits():
    return find_all_outfits_use_case.run()