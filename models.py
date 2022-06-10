from pydantic import BaseModel

# Criar Model
class Filme(BaseModel):
    id: int
    nome: str
    genero: str
    lancamento: str