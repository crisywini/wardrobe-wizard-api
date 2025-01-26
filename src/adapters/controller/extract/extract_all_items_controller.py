from typing import Optional

from fastapi import APIRouter, Query

from src.adapters.controller.model.mappers.item_mapper import map_to_dtos
from src.adapters.gateway.mongodb.find.find_all_items_mongodb_gateway import FindAllItemsMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.find.find_all_items_use_case import FindAllItemsUseCase

from src.adapters.gateway.mongodb.find.find_all_items_by_category_mongodb_gateway import \
    FindAllItemsByCategoryMongoDBGateway
from src.use_cases.find.find_all_items_by_category_use_case import FindAllItemsByCategoryUseCase


router = APIRouter()
mongodb_instance = get_mongodb_instance()

find_all_items_mongodb_gateway = FindAllItemsMongoDBGateway(mongodb_instance)
find_all_items_use_case = FindAllItemsUseCase(find_all_items_mongodb_gateway)

find_all_items_by_category_mongodb_gateway = FindAllItemsByCategoryMongoDBGateway(mongodb_instance)
find_all_items_by_category_use_case = FindAllItemsByCategoryUseCase(find_all_items_by_category_mongodb_gateway)



@router.get(path="/items")
def get_items(category: Optional[str] = Query(None)):
    if category:
        return map_to_dtos(find_all_items_by_category_use_case.run(category))
    all_items = find_all_items_use_case.run()
    return map_to_dtos(all_items)