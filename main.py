from fastapi import FastAPI, HTTPException, Query
from utils.embrapa import scrap_and_find_links
import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get('/Produção/')
async def get_website_links():
    return {'links': scrap_and_find_links("Produção")}

@app.get('/Processamento/')
async def get_website_links():
    return {'links': scrap_and_find_links("Processamento")}

@app.get('/Comercialização/')
async def get_website_links():
    return {'links': scrap_and_find_links("Comercialização")}

@app.get('/Importação/')
async def get_website_links():
    return {'links': scrap_and_find_links("Importação")}

@app.get('/Exportação/')
async def get_website_links():
    return {'links': scrap_and_find_links("Exportação")}
