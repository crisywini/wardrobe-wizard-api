from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from router import item_router, outfit_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.include_router(item_router.router)
app.include_router(outfit_router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.mount("/images", StaticFiles(directory="static/images"), name="images")


@app.get("/")
def read_root():
    return {"Hello": "World"}

