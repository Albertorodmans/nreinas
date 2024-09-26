from sqlalchemy import JSON, create_engine, Column, Integer, Sequence 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class Solution(Base):
    __tablename__ = 'solutions'
    id = Column("id",Integer, Sequence('solution_id_seq'), primary_key=True)
    n = Column("n",Integer)
    numsolutions = Column("numsolutions",Integer)
    board = Column("board",JSON)

def save_solution(n, board,numsolutions):
    session=conection()
    solution = Solution(n=n, board=board,numsolutions=numsolutions)
    session.add(solution)
    session.commit()
    session.close()
    
def check_solution(nreinas):
    session=conection()
    count=session.query(Solution).filter(Solution.n==nreinas).count()
    if count==0:
        session.commit()
        session.close()
        return None,False
    register=session.query(Solution).filter(Solution.n==nreinas)
    for r in register:
        board=r.board
    session.commit()
    session.close()
    return board,True
    
    
def conection():
    engine = create_engine("postgresql://root:Cbg9Xay9xtN@127.0.0.1:5433/nreinas")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
