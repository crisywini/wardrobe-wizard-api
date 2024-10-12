from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb://localhost:27017/")
db = client["wardrobe_db"]  


items_collection = db["items"]
items = [
    {
        "name": "Camisa blanca",
        "category": "Camisa",
        "color": "Blanco",
        "style": "Casual",
        "brand": "Zara",
        "season": "Primavera",
        "image_url": "https://mis-imagenes.com/camisa_blanca.jpg"
    },
    {
        "name": "Pantalón negro",
        "category": "Pantalón",
        "color": "Negro",
        "style": "Formal",
        "brand": "H&M",
        "season": "Otoño",
        "image_url": "https://mis-imagenes.com/pantalon_negro.jpg"
    },
    {
        "name": "Chaqueta de cuero",
        "category": "Chaqueta",
        "color": "Negro",
        "style": "Rockero",
        "brand": "Levi's",
        "season": "Invierno",
        "image_url": "https://mis-imagenes.com/chaqueta_cuero.jpg"
    },
    {
        "name": "Vestido rojo",
        "category": "Vestido",
        "color": "Rojo",
        "style": "Elegante",
        "brand": "Gucci",
        "season": "Verano",
        "image_url": "https://mis-imagenes.com/vestido_rojo.jpg"
    },
    {
        "name": "Zapatos deportivos",
        "category": "Calzado",
        "color": "Blanco",
        "style": "Deportivo",
        "brand": "Nike",
        "season": "Todo el año",
        "image_url": "https://mis-imagenes.com/zapatos_deportivos.jpg"
    }
]

# Insertar los items en la colección
result = items_collection.insert_many(items)

# Imprimir los IDs de los documentos insertados
print(f"Documentos insertados: {result.inserted_ids}")