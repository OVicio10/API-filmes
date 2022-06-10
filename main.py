from fastapi import FastAPI
from models import Filme


app = FastAPI()

# raiz
@app.get("/")
def raiz():
    return {"Ola" : "mundo"}

# Base de dados
base_de_dados = [
    Filme(id=1,nome="Homem Aranha",genero="Aventura",lancamento="2021"),
    Filme(id=2,nome="Doutor Estranho",genero="Aventura",lancamento="2022")
]

# Get All
@app.get("/filmes")
def get_todos_os_filmes():
    return base_de_dados