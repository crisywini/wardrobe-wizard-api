class Outfit:
    
    def __init__(self, id: str, name: str, items: list, category: str):
        self.id = id
        self.name = name
        self.items = items
        self.category = category
        self.default_image_url = ""
        self.pictures_urls = []
    
    def __str__(self):
        return f"Outfit(id: {self.id}, name: {self.name}, items: {self.items})"