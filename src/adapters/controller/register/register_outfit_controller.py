from fastapi import APIRouter

from src.adapters.controller.model.mappers.outfit_mapper import map_to_entity
from src.adapters.controller.model.outfit_dto import OutfitDto
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.adapters.gateway.mongodb.save.save_outfit_mongodb_gateway import SaveOutfitMongoDBGateway
from src.use_cases.save.save_outfit_use_case import SaveOutfitUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

save_outfit_mongodb_gateway = SaveOutfitMongoDBGateway(mongodb_instance)
save_outfit_mongodb_use_case = SaveOutfitUseCase(save_outfit_mongodb_gateway)


@router.post(path="/outfits")
def get_all_outfits(outfit: OutfitDto):
    return save_outfit_mongodb_use_case.run(map_to_entity(outfit))