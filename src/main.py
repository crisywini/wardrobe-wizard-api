from fastapi import FastAPI
from src.adapters.controller.register import register_item_controller, register_outfit_controller
from src.adapters.controller.extract import extract_all_items_controller, extract_all_outfits_controller, \
    extract_outfit_by_id_controller, extract_item_by_id_controller
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(register_item_controller.router)
app.include_router(register_outfit_controller.router)
app.include_router(extract_item_by_id_controller.router)
app.include_router(extract_all_items_controller.router)
app.include_router(extract_outfit_by_id_controller.router)
app.include_router(extract_all_outfits_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.mount("/images", StaticFiles(directory="static/images"), name="images")


@app.get("/")
def read_root():
    return {"Hello": "World"}
