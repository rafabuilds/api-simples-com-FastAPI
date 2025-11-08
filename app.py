from fastapi import FastAPI 

app = FastAPI()

PRODUTOS = [
    {
        "id": 1,
        "sku": "FIT-BIO-000",
        "nome": "Fitmass Bioscan",
        "descricao": "Balança de bioimpedância com tela de x polegadas.",
        "preco": 8599.00, # Preços devem ser números, definidos como float ou decimal.
        "tipo": "Hardware",
        "recorrencia": "Não se aplica",
        "ativo": True
    },
    {
        "id": 2,
        "sku": "FIT-SYS-PRO-000",
        "nome": "Fitmass System - Plano Pro (Academia)", # Ou para profissionais como nutricionais, personal trainer, etc...
        "descricao": "App de gestão de alunos para personal trainers (até 500 alunos).",
        "preco": 299.90,
        "tipo": "Software",
        "recorrencia": "Mensal", # Pode ser trimestral ou anual, também.
        "ativo": True 
    }
]

# #@app.get("/")
# async def root(): 
#     """this is the root path."""
#     return {"message": "Hello, World!"}

