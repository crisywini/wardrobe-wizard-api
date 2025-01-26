from pydantic import BaseModel
from typing import List, Optional

class OutfitDto(BaseModel):
    id: str
    name: str
    category: str
    items: List[dict] = []  
    
    def add_item(self, item: dict):
        self.items.append(item)

    def __str__(self):
        return f"Outfit: {self.name} with {len(self.items)} items"

    def show_outfit(self):
        for item in self.items:
            print(item)
