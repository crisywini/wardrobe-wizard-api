class Outfit:
    
    def __init__(self, id: str, name: str, items: list, category: str):
        self.id = id
        self.name = name
        self.items = items
        self.category = category
    
    def __str__(self):
        return f"Outfit(id: {self.id}, name: {self.name}, items: {self.items})"