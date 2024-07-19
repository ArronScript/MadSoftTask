from contextlib import asynccontextmanager

from fastapi import FastAPI
from api_service.private_api import router as private_router
from .public_api import router as public_router

app = FastAPI()

app.include_router(public_router, prefix='/public', tags=['Public'])
app.include_router(private_router, prefix='/private', tags=['Private'])


@app.get("/")
async def root():
    return {"message": "Welcome to the Memes API"}
