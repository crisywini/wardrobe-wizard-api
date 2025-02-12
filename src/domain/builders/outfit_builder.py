from src.domain.builders.builder import Builder
from src.domain.entities.outfit import Outfit

class OutfitBuilder(Builder):
    
    def __init__(self):
        self.id = "id"
        self.name = "name"
        self.items = []
        self.category = ""
        self.default_image_url = ""
        
    def set_id(self, id):
        self.id = str(id)
        return self

    def set_name(self, name):
        self.name = name
        return self 

    def set_items(self, items):
        self.items = items
        return self

    def set_category(self, category):
        self.category = category
        return self

    def set_default_image_url(self, default_image_url):
        self.default_image_url = default_image_url
        return self

    def build(self):
        return Outfit(self.id, self.name, self.items, self.category, self.default_image_url)