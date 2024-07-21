from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Definindo o modelo de dados para a resposta
class PageData(BaseModel):
    url: str
    html: str
    links: list

# Função para extrair os links de uma página web
def extract_links(url: str) -> PageData:
    try:
        # Fazendo a requisição HTTP para a URL
        response = requests.get(url)
        
        # Verificando se a resposta é bem-sucedida
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error")
        
        # Fazendo o parsing do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraindo todos os links da página
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Retornando os dados extraídos como um objeto PageData
        return PageData(
            url=url,
            html=soup.prettify(),
            links=links
        )
    except requests.exceptions.RequestException as e:
        # Lidando com possíveis erros de requisição
        raise HTTPException(status_code=500, detail=str(e))

# Definindo o endpoint da API para extrair links
@app.get("/extract_links", response_model=PageData)
async def get_links(url: str = Query(..., description="http://vitibrasil.cnpuv.embrapa.br/download/")):
    try:
        # Chamando a função de extração de links
        data = extract_links(url)
        return data
    except HTTPException as http_exc:
        # Lidando com exceções HTTP
        raise http_exc
    except Exception as e:
        # Lidando com outras exceções
        raise HTTPException(status_code=500, detail=str(e))

# Código para rodar a aplicação usando uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
