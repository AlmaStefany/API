#teste pela milesima veeeeeeezzzzzz

"""Instalção inicial:
abrir o terminal e dar o seguinte comando: pip install fastapi
apos a instalação, digitar no terminal: pip install uvicorn."""

'''Testar se a APi esta no ar: 
vc precisa abrir o terminal e digitar: uvicorn nome do arquivo (no meu caso aqui é
main) e o nome do aplicativo (no caso aqui é app) e por ultimo digitar --reload então fica: uvicorn main:app --reload'''

from fastapi import FastAPI, HTTPException, Query
from utils.scraping import scrap_website
from utils.find_links import find_links_at_level_one, find_links_at_level_two

app = FastAPI()
@app.get('/links')
async def get_website_links():
    #faz o scraping do site especificado.
    website_content = scrap_website('https://iseb3.com.br/respostas-em-planilhas')

    #verifica se há conteúdo no site
    if not website_content:
        #lança uma exceção
        raise HTTPException(status_code=404, detail='nenhum conteúdo encontrado')

    #extrai os links do conteúdo da pagina no primeiro nivel
    links = find_links_at_level_one(website_content)

    #verifica se tem link extraidos
    if not links:
        raise HTTPException(status_code=404, detail='nenhum conteúdo encontrado')

    #retorna o link contraido com resposta
    return {'links': links}
