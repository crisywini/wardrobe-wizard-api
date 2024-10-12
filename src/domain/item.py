from pydantic import BaseModel, Field
from typing import Optional



class Item(BaseModel):
    id: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    color: Optional[str] = Field(None)
    style: Optional[str] = Field(None)
    brand: Optional[str] = Field(None)
    season: Optional[str] = Field(None)
    image_url: Optional[str] = Field(None)
    
    def __str__(self):
        return f"{self.name} ({self.category}, {self.color}, {self.style})"