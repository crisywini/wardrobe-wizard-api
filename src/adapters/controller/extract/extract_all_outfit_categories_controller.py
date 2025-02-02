from typing import Optional

from fastapi import APIRouter, Query

from src.adapters.gateway.mongodb.find.find_all_outfits_by_category_mongodb_gateway import \
    FindAllOutfitsByCategoryMongoDBGateway
from src.adapters.gateway.mongodb.find.find_all_outfits_mongodb_gateway import FindAllOutfitsMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.find.find_all_outfit_categories_use_case import FindAllOutfitCategoriesUseCase
from src.use_cases.find.find_all_outfits_by_category_use_case import FindAllOutfitsByCategoryUseCase
from src.use_cases.find.find_all_outfits_use_case import FindAllOutfitsUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

find_all_outfits_mongodb_gateway = FindAllOutfitsMongoDBGateway(mongodb_instance)
find_all_outfits_categories_use_case = FindAllOutfitCategoriesUseCase(find_all_outfits_mongodb_gateway)


@router.get(path="/outfits/categories")
def get_all_outfits():
    return find_all_outfits_categories_use_case.run()
