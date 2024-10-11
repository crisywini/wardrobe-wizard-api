from pydantic import BaseModel


class Item(BaseModel):
    id: str
    name: str
    category: str
    color: str
    style: str
    brand: str
    season: str
    image_url: str
    
    def __str__(self):
        return f"{self.name} ({self.category}, {self.color}, {self.style})"