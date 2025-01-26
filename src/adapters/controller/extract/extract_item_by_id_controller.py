from fastapi import APIRouter

from src.adapters.gateway.mongodb.find.find_item_by_id_mongodb_gateway import FindItemByIdMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.find.find_item_by_id_use_case import FindItemByIdUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

find_item_by_id_mongodb_gateway = FindItemByIdMongoDBGateway(mongodb_instance)
find_item_by_id_use_case = FindItemByIdUseCase(find_item_by_id_mongodb_gateway)

@router.get("/items/{item_id}")
def get_item(item_id: str):
    return find_item_by_id_use_case.run(item_id)