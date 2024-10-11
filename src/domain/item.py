from pydantic import BaseModel

class Item(BaseModel):

    def __init__(self, name, category, color, style, brand, season):
        self.id = 0
        self.name = name
        self.category = category
        self.color = color
        self.style = style
        self.brand = brand
        self.season = season
    
    def __str__(self):
        return f"{self.name} ({self.category}, {self.color}, {self.style})"