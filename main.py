#teste pela milesima veeeeeeezzzzzz

"""Instalção inicial:
abrir o terminal e dar o seguinte comando: pip install fastapi
apos a instalação, digitar no terminal: pip install uvicorn."""

'''Testar se a APi esta no ar: 
vc precisa abrir o terminal e digitar: uvicorn nome do arquivo (no meu caso aqui é
main) e o nome do aplicativo (no caso aqui é app) e por ultimo digitar --reload então fica: uvicorn main:app --reload'''

from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def home():
    return'teste de API no ar'

#vou mandar meu primeiro commit aqui pra testar e chamar de base