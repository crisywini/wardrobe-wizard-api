class Item:
    
    def __init__(self, id:str, name:str, category: str, color:str, style: str, brand:str, season: str, image_url: str):
        self.id = id
        self.name = name
        self.category = category
        self.color = color
        self.style = style
        self.brand = brand
        self.season = season
        self.image_url = image_url
        
    def __str__(self):
        return f"Item(id={self.id}, name={self.name}, category={self.category}, color={self.color}, style={self.style}, brand={self.brand}, season={self.season}, image_url={self.image_url})"

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "category": self.category,
            "color": self.color,
            "style": self.style,
            "brand": self.brand,
            "season": self.season,
            "image_url": self.image_url
        }