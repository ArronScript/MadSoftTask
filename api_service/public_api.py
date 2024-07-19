from fastapi import FastAPI, APIRouter
from db_service.db import db_service


router = APIRouter()


@router.get("/memes/")
async def read_memes(skip: int = 0, limit: int = 10):
    mems = db_service.get_memes(skip, limit)
    return mems


@router.get("/memes/{id}")
async def read_mem(id: int):
    mem = db_service.get_mem(id)
    if mem:
        return mem
    return {'error': 'Mem not found'}
