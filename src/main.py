from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from router import item_router, outfit_router

app = FastAPI()
app.include_router(item_router.router)
app.include_router(outfit_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload/")
async def upload_item(image: UploadFile = File(...)):
    file_location = f"{image.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())
    
    return JSONResponse(content={"filename": image.filename})
