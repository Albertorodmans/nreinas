from .models import Solution
from .database import conection
session=conection()
def save_solution(n, board,numsolutions):
    solution = Solution(n=n, board=board,numsolutions=numsolutions)
    session.add(solution)
    session.commit()
    session.close()
    
def check_solution(nreinas):
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
    