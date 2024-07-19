from pydantic import BaseModel


class MemCreate(BaseModel):
    text: str

class MemUpdate(BaseModel):
    text: str
    image_url: str