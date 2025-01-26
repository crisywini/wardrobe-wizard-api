from typing import Optional

from fastapi import APIRouter, Query

from src.adapters.gateway.mongodb.find.find_all_outfits_by_category_mongodb_gateway import \
    FindAllOutfitsByCategoryMongoDBGateway
from src.adapters.gateway.mongodb.find.find_all_outfits_mongodb_gateway import FindAllOutfitsMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.find.find_all_outfits_by_category_use_case import FindAllOutfitsByCategoryUseCase
from src.use_cases.find.find_all_outfits_use_case import FindAllOutfitsUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

find_all_outfits_mongodb_gateway = FindAllOutfitsMongoDBGateway(mongodb_instance)
find_all_outfits_use_case = FindAllOutfitsUseCase(find_all_outfits_mongodb_gateway)

find_all_outfits_by_category_mongodb_gateway = FindAllOutfitsByCategoryMongoDBGateway(mongodb_instance)
find_all_outfits_by_category_use_case = FindAllOutfitsByCategoryUseCase(find_all_outfits_by_category_mongodb_gateway)

@router.get(path="/outfits")
def get_all_outfits(category: Optional[str] = Query(None)):
    if category:
        return find_all_outfits_by_category_mongodb_gateway.run(category)
    return find_all_outfits_use_case.run()