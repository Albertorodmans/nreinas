from sqlalchemy import create_engine
from .models import Base
from sqlalchemy.orm import sessionmaker
import os

    
def conection():
    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
