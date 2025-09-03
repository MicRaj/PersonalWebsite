from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.data import router as data_router
from app.core.database import SessionDep, create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(data_router)

# Allowing CORS from the specific origin (localhost:5173) or any origin
origins = ["*"]  # Or you can use localhost and 127.0.0.1 as the origin

# Adding CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify the frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
