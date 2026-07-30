from app.database.base import Base
from app.database.connection import engine

# Import all models here
from app.models.message import Message
from app.models.memory import Memory

def create_tables():
    Base.metadata.create_all(bind=engine)