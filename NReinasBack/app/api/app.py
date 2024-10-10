
from .endpoints.nreinas import solve_n_queens,router
from fastapi import FastAPI 
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
  

app.include_router(router)
# Ejemplo de uso
if __name__ == "__main__":
    n = 8
    print(solve_n_queens(n))

