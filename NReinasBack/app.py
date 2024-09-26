import json
from posixpath import split
from database import save_solution,check_solution
from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
]


tags_metadata = [
    {
        "name": "nreinas",
        "description": "Metodo POST, introduzca el número 'N' de Reinas a resolver en el tablero",
    }
]
app = FastAPI(
    title="Problema de las ocho reinas",
    description="El problema de las ocho reinas es un pasatiempo que consiste en poner ocho reinas en el tablero de ajedrez sin que se amenacen. Fue propuesto por el ajedrecista alemán Max Bezzel en 1848",
    summary="Problema soluconado con Backtraking",
    version="0.0.1",
    terms_of_service="",
    contact={
        "name": "Alberto Rodriguez Mancera",
        "url": "http://www.savewalterwhite.com/",
        "email": "alberto.rodmans@gmail.com",
    },
    openapi_tags=tags_metadata,
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class QueensInput(BaseModel):
    n: int
    
@app.post("/resolver", tags=["nreinas"])
def get_solutions(input: QueensInput):
    solution,flag = check_solution(input.n)
    if flag:
       return json.loads(solution)
    solutions,numersolution = solve_n_queens(input.n)
    return {"number_solutions":numersolution,"solutions": solutions} 


def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True

    def solve_util(board, col):
        if col >= n:
            solutions.append([''.join(row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                solve_util(board, col + 1)
                board[i][col] = '.'

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_util(board, 0)
    save_solution(n,{"number_solutions":len(solutions),"solutions":solutions},len(solutions))
    return solutions,len(solutions)

# Ejemplo de uso
if __name__ == "__main__":
    n = 8
    print(solve_n_queens(n))

