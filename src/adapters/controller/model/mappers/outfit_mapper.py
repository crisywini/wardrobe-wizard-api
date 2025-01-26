from src.adapters.controller.model.outfit_dto import OutfitDto
from src.domain.builders.outfit_builder import OutfitBuilder

def map_to_entity(outfit_dto: OutfitDto):
    return OutfitBuilder().set_id(outfit_dto.id).set_name(outfit_dto.name).set_category(outfit_dto.category).set_items(
        outfit_dto.items)
