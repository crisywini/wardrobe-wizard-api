from domain.item import Item

class ItemService:

    def __init__(self, repository):
        self.repository = repository

    def save(self, item):
        return str(self.repository.insert_item(item))

    def get_all(self):
        return self.repository.find_all_items()

    def delete_by_id(self, id):
        return self.repository.delete_one_item(id)

    def update(self, id, item):
        return self.respository.update_one_item(id, item)

    def get_by_id(self, id):
        entity = self.repository.get_one_item_by_id(id)
        item = Item(
                id=str(entity.get("_id")),
                name=entity.get("name"),
                category=entity.get("category"),
                color=entity.get("color"),
                style=entity.get("style"),
                brand=entity.get("brand"),
                season=entity.get("season"),
                image_url=entity.get("image_url")  
            )
        return item