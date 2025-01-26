class Outfit:
    
    def __init__(self, id: str, name: str, items: list):
        self.id = id
        self.name = name
        self.items = items
    
    def __str__(self):
        return f"Outfit(id: {self.id}, name: {self.name}, items: {self.items})"