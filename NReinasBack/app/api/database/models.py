from sqlalchemy import Column, Integer, Sequence ,JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Solution(Base):
    __tablename__ = 'solutions'
    id = Column("id",Integer, Sequence('solution_id_seq'), primary_key=True)
    n = Column("n",Integer)
    numsolutions = Column("numsolutions",Integer)
    board = Column("board",JSON)