import os
from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.posts import router as post_router
from app.api.users import router as user_router
from app.core.database import SessionDep, create_db_and_tables
from app.core.db_init import create_initial_admin


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    try:
        create_initial_admin()
    except Exception as e:
        print(f"Error creating admin user: {e}")
        raise
    yield


APP_MODE = os.getenv("APP_MODE", "development")
docs_url = None if APP_MODE == "production" else "/docs"
redoc_url = None if APP_MODE == "production" else "/redoc"
openapi_url = None if APP_MODE == "production" else "/openapi.json"
app = FastAPI(
    docs_url=docs_url,
    redoc_url=redoc_url,
    openapi_url=openapi_url,
    lifespan=lifespan,
    root_path="/api",
)

app.include_router(post_router)
app.include_router(user_router)

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
