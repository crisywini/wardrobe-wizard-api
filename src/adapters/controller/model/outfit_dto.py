from pydantic import BaseModel
from typing import List

class OutfitDto(BaseModel):
    id: str = None
    name: str
    category: str
    items: List[dict] = []
    default_image_url: str = None
    
    def add_item(self, item: dict):
        self.items.append(item)

    def __str__(self):
        return f"Outfit: {self.name} with {len(self.items)} items"

