from fastapi import APIRouter, UploadFile, Form, File
from starlette.responses import JSONResponse

from src.adapters.controller.config.constants import URL_IMAGE_DEFAULT_FE_PATH
from src.adapters.controller.model.item_dto import ItemDto
from src.adapters.controller.model.mappers.item_mapper import map_to_entity, map_to_dto
from src.adapters.gateway.mongodb.mongo_client_config import get_mongodb_instance
from src.adapters.gateway.mongodb.save.save_item_mongdb_gateway import SaveItemMongoDBGateway
from src.use_cases.save.save_item_use_case import SaveItemUseCase

router = APIRouter()
mongodb_instance = get_mongodb_instance()

save_item_mongodb_gateway = SaveItemMongoDBGateway(mongodb_instance)
save_item_use_case = SaveItemUseCase(save_item_mongodb_gateway)


@router.post(path="/items")
async def register_item(file: UploadFile = File(...), item: str = Form(...)):
    file_location = f"{URL_IMAGE_DEFAULT_FE_PATH}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    item_data = ItemDto.model_validate_json(item)
    item_data.image_url = f"/images/{file.filename}"

    entity = save_item_use_case.run(map_to_entity(item_data))

    return JSONResponse(
        status_code=201,
        content=map_to_dto(entity)
    )
