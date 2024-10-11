from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload/")
async def upload_image(image: UploadFile = File(...)):
    file_location = f"{image.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())
    
    return JSONResponse(content={"filename": image.filename})
