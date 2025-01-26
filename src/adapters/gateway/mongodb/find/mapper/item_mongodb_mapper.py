from src.domain.builders.item_builder import ItemBuilder


def map_to_entity(item_mongodb):
    builder = ItemBuilder().set_id(item_mongodb.get("_id")).set_name(item_mongodb.get("name")).set_category(
        item_mongodb.get("category")).set_color(item_mongodb.get("color")).set_style(item_mongodb.get("style")).set_brand(
        item_mongodb.get("brand")).set_season(item_mongodb.get("season")).set_image_url(item_mongodb.get("image_url"))
    return builder.build()