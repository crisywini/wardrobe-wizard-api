from fastapi import APIRouter

from src.adapters.controller.model.mappers.item_mapper import map_to_dtos
from src.adapters.gateway.mongodb.find.find_all_items_mongodb_gateway import FindAllItemsMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.find.find_all_items_use_case import FindAllItemsUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

find_all_items_mongodb_gateway = FindAllItemsMongoDBGateway(mongodb_instance)
find_all_items_use_case = FindAllItemsUseCase(find_all_items_mongodb_gateway)

@router.get(path="/items")
def get_items():
    all_items = find_all_items_use_case.run()
    return map_to_dtos(all_items)