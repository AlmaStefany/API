#teste pela milesima veeeeeeezzzzzz

"""Instalção inicial:
abrir o terminal e dar o seguinte comando: pip install fastapi
apos a instalação, digitar no terminal: pip install uvicorn."""
import logging

import utils.scraping

'''Testar se a APi esta no ar: 
vc precisa abrir o terminal e digitar: uvicorn nome do arquivo (no meu caso aqui é
main) e o nome do aplicativo (no caso aqui é app) e por ultimo digitar --reload então fica: uvicorn main:app --reload'''

from fastapi import FastAPI, HTTPException, Query
from utils.scraping import scrap_website
from utils.find_links import find_links_at_level_one, find_links_at_level_two

logging.basicConfig(level=logging.INFO)

app = FastAPI()
@app.get('/links/')
async def get_website_links():
    #faz o scraping do site especificado.
    website_content = scrap_website('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01')

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

@app.get('/links2/')
async def get_website_links2(link: str = Query(..., description='URL do link para acessar')):
    """
       Rota GET para obter links do segundo nível de um website.

       Args:
           link (str): A URL do link para acessar.

       Returns:
           dict: Um dicionário contendo uma lista de links encontrados.

       Raises:
           HTTPException: Se o parâmetro 'link' estiver ausente, ou se nenhum conteúdo ou link for encontrado.
       """
    # Registra o link recebido
    logging.info(f'recebendo link: {link}')

    if not link:
        raise HTTPException(status_code=400, detail='link é obrigatorio')

    #faz o scraping do site especificado pelo link
    website_content = utils.scraping.scrap_website(link)

    if not website_content:
        # lança uma exceção
        raise HTTPException(status_code=404, detail='nenhum conteúdo encontrado')

    # extrai os links do conteúdo da pagina no primeiro nivel
    links = find_links_at_level_two(website_content)

    if not links:
        raise HTTPException(status_code=404, detail='nenhum link encontrado')

    return {'links': links}








