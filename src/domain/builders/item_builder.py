from builder import Builder
from src.domain.entities.item import Item

class ItemBuilder(Builder):
    def __init__(self):
        self._id = None
        self._name = None
        self._category = None
        self._color = None
        self._style = None
        self._brand = None
        self._season = None
        self._image_url = None

    def id(self, id: str):
        self._id = id
        return self

    def name(self, name: str):
        self._name = name
        return self

    def category(self, category: str):
        self._category = category
        return self

    def color(self, color: str):
        self._color = color
        return self

    def style(self, style: str):
        self._style = style
        return self

    def brand(self, brand: str):
        self._brand = brand
        return self

    def season(self, season: str):
        self._season = season
        return self

    def image_url(self, image_url: str):
        self._image_url = image_url
        return self

    def build(self):
        return Item(
            id=self._id,
            name=self._name,
            category=self._category,
            color=self._color,
            style=self._style,
            brand=self._brand,
            season=self._season,
            image_url=self._image_url
        )