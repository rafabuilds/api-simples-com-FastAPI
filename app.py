from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

PRODUTOS = [
    {
        "id": 1,
        "codigo_produto": "FIT-BIO-001",
        "nome": "Fitmass Bioscan",
        "descricao": "Balança de bioimpedância com tela de x polegadas.",
        "preco": 8599.00, # Preços devem ser números, definidos como float ou decimal.
        "tipo": "Hardware",
        "recorrencia": "Pagamento único",
        "disponivel": True
    },
    {
        "id": 2,
        "codigo_produto": "FIT-POC-001",
        "nome": "Fitmass Pocket", 
        "descricao": "App de gestão de alunos para personal trainers (até 100 alunos) ou nutricionistas.",
        "preco": 49.90,
        "tipo": "Software",
        "recorrencia": "Mensal", # Pode ser trimestral ou anual, também.
        "disponivel": True 
    }
]

class Produto(BaseModel):
    """Classe Produto."""
    id: int
    codigo_produto: str
    nome: str
    descricao: str
    preco: float
    tipo: str
    recorrencia: str
    disponivel: Optional[bool] = True

@app.get("/produtos", tags=["produtos"])
def listar_produtos() -> list:
    """Listar Produtos."""
    return PRODUTOS
     
@app.get("/produtos/disponiveis", tags=["produtos"])
def listar_produtos_disponiveis() -> list:
    """Listar Produtos Disponíveis."""
    produtos_disponiveis = []
    for produto in PRODUTOS:
        if produto["disponivel"]:
            produtos_disponiveis.append(produto)    
    return produtos_disponiveis     
        
@app.get("/produtos/{produto_id}", tags=["produtos"])
def obter_produtos(produto_id: int) -> dict:
    """Obter Produtos."""
    for produto in PRODUTOS:
        if produto["id"] == produto_id:
            return produto
    return None

@app.post("/produtos", tags=["produtos"])
def criar_produto(produto: Produto) -> dict:
    """Criar Produtos."""
    PRODUTOS.append(produto)
    return produto

@app.put("/produtos/{produto_id}", tags=["produtos"])
def atualizar_produto(produto_id: int, produto: Produto) -> dict:
    """Atualizar Produtos."""
    for index, p in enumerate(PRODUTOS):
        if p["id"] == produto_id:
            PRODUTOS[index] = produto
            return produto
    return None

@app.delete("/produtos/{produto_id}", tags=["produtos"])
def deletar_produto(produto_id: int) -> dict:
    """Deletar Produtos."""
    for index, produto in enumerate(PRODUTOS):
        if produto["id"] == produto_id:
            del PRODUTOS[index]
            return {"message": "Produto deletado com sucesso."}
    return {"message": "Produto não encontrado."}

