from pydantic import BaseModel

class Outfit(BaseModel):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Outfit: {self.name} with {len(self.items)} items"

    def show_outfit(self):
        for item in self.items:
            print(item)
