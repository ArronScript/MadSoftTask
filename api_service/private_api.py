from fastapi import File, UploadFile, APIRouter

from media_service.media import media_service

from db_service.db import db_service

from api_service.shemas.memes_shema import MemUpdate, MemCreate

router = APIRouter()


@router.post("/memes/")
async def create_mem(mem: MemCreate, file: UploadFile = File(...)):
    if media_service.upload_file('memes', file.filename, file.file):
        mem = db_service.create_mem(mem.text, f'http://localhost:9000/memes/{file.filename}')
        return mem
    else:
        return {'error': 'Failed to upload file'}


@router.put("/memes/{id}")
async def update_mem(id: int, mem: MemUpdate):
    mem = db_service.update_mem(id, mem.text, mem.image_url)
    if mem:
        return mem
    return {'error': 'Mem not found'}


@router.delete("/memes/{id}")
async def delete_mem(id: int):
    if db_service.delete_mem(id):
        return {'message': 'Mem deleted'}
    return {'error': 'Mem not found'}
