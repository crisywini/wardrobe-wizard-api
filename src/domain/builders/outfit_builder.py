from src.domain.entities.outfit import Outfit
from builder import Builder 

class OutfitBuilder(Builder):
    
    def __init__(self):
        self.id = "id"
        self.name = "name"
        self.items = []
        self.category = ""
        
    def id(self, id):
        self.id = id
        return self

    def name(self, name):
        self.name = name
        return self 

    def items(self, items):
        self.items = items
        return self

    def category(self, category):
        self.category = category
        return self

    def build(self):
        return Outfit(self.id, self.name, self.items)