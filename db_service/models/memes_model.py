
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Mem(Base):
    __tablename__ = 'memes'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    image_url = Column(String)