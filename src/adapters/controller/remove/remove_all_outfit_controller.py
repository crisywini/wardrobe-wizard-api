from fastapi import APIRouter

from src.adapters.gateway.mongodb.delete.delete_all_outfits_mongodb_gateway import DeleteAllOutfitsMongoDBGateway
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.use_cases.delete.delete_all_outfits_use_case import DeleteAllOutfitsUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

delete_all_outfits_mongodb_gateway = DeleteAllOutfitsMongoDBGateway(mongodb_instance)
delete_all_outfits_use_case = DeleteAllOutfitsUseCase(delete_all_outfits_mongodb_gateway)

@router.delete(path="/outfits")
def remove_all_items():
    return {
        "rows_deleted": delete_all_outfits_use_case.run()
    }
