import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

from routes import bolt_router, vasarlas_router, vasarlas_tetel_router, cikkek_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000/",
    "http://127.0.0.1:3000",
    "localhost",
    "localhost:3000",
    "127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient('mongodb+srv://Vonalzo:fPMXNUkXA4REyhCa@cluster0.qlfwyae.mongodb.net/?retryWrites=true&w=majority')
    app.database = app.mongodb_client['pelda']
    print("Connected to the MongoDB database!")
    print(app.database.name)

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def root():
    return {"haha"}

app.include_router(bolt_router, tags=["bolt"], prefix="/bolt")
app.include_router(vasarlas_router, tags=["vasarlas"], prefix="/vasarlas")
app.include_router(vasarlas_tetel_router, tags=["vasarlas_tetel"], prefix="/vasarlas_tetel")
app.include_router(cikkek_router, tags=["cikkek"], prefix="/cikkek")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)