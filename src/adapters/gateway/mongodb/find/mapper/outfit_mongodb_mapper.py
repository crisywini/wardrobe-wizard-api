from src.domain.builders.outfit_builder import OutfitBuilder


def map_to_entity(outfit):
    return OutfitBuilder().set_id(outfit.get("_id")).set_name(outfit.get("name")).set_category(
        outfit.get("category")).set_items(outfit.get("items")).set_default_image_url(outfit.get("default_image_url")).build()
