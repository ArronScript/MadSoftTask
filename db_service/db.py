import socket

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.memes_model import Base, Mem


class DBService:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_memes(self, skip=0, limit=10):
        return self.session.query(Mem).offset(skip).limit(limit).all()

    def get_mem(self, id: int):
        return self.session.query(Mem).filter(Mem.id == id).first()

    def create_mem(self, text, image_url):
        mem = Mem(text=text, image_url=image_url)
        self.session.add(mem)
        self.session.commit()
        return mem

    def update_mem(self, id: int, text, image_url):
        mem = self.session.query(Mem).filter(Mem.id == id).first()
        if mem:
            mem.text = text
            mem.image_url = image_url
            self.session.commit()
            return mem
        return None

    def delete_mem(self, id: int):
        mem = self.session.query(Mem).filter(Mem.id == id).first()
        if mem:
            self.session.delete(mem)
            self.session.commit()
            return True
        return False


db_service = DBService(f"postgresql+psycopg2://postgres:kiss@db/memes")
