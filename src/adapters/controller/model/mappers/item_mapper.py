from src.adapters.controller.model.item_dto import ItemDto
from src.domain.builders.item_builder import ItemBuilder


def map_to_entity(item_dto: ItemDto):
    return ItemBuilder.set_id(item_dto.id).set_name(item_dto.name).set_category(
        item_dto.category).set_color(
        item_dto.color).set_style(item_dto.style).set_brand(item_dto.brand).set_season(
        item_dto.season).set_image_url(
        item_dto.image_url).build()
