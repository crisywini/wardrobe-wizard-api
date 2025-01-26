from src.domain.entities.outfit import Outfit
from builder import Builder 

class OutfitBuilder(Builder):
    
    def __init__(self):
        self.id = "id"
        self.name = "name"
        self.items = []
        self.category = ""
        
    def set_id(self, id):
        self.id = id
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

    def build(self):
        return Outfit(self.id, self.name, self.items)