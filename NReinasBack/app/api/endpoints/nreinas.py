
from ..database.crud import check_solution, save_solution
from fastapi import APIRouter,HTTPException

from pydantic import BaseModel
import json

router=APIRouter(
       prefix="/resolver"
)
 

class QueensInput(BaseModel):
    n: int
    
@router.post("/numreinas", tags=["nreinas"])
def get_solutions(input: QueensInput):
    print(type(input.n))
    if type(input.n) is not int:
        raise HTTPException(status_code=400, detail="dato erróneo, favor de colocar un valor entero")
    solution,flag = check_solution(input.n)
    if flag:
       return solution
    solutions,numersolution = solve_n_queens(input.n)
    return {"number_solutions":numersolution,"solutions": solutions} 


def solve_n_queens(num_reinas):
    def is_safe(board, row, col):
        for fila in range(col):
            if board[row][fila] == 'Q':
                return False
        for fila, columna in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[fila][columna] == 'Q':
                return False
        for fila, columna in zip(range(row, num_reinas), range(col, -1, -1)):
            if board[fila][columna] == 'Q':
                return False
        return True

    def solve_util(board, col):
        if col >= num_reinas:
            solutions.append([''.join(row) for row in board])
            return
        for filas in range(num_reinas):
            if is_safe(board, filas, col):
                board[filas][col] = 'Q'
                solve_util(board, col + 1)
                board[filas][col] = '.'

    solutions = []
    board = [['.' for _ in range(num_reinas)] for _ in range(num_reinas)]
    solve_util(board, 0)
    save_solution(num_reinas,{"number_solutions":len(solutions),"solutions":solutions},len(solutions))
    return solutions,len(solutions)