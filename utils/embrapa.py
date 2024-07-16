from fastapi import HTTPException  # Importa a classe HTTPException da biblioteca FastAPI para tratar exceções HTTP
from utils.scraping import scrap_website
from utils.find_links import find_links_at_level_one

# Servidor que contém todos os arquivos
servidor_ftp = "http://vitibrasil.cnpuv.embrapa.br/download/"

# Dicionário representando as aba do site da Embrapa
embrapa = {
    "Produção":        ["Producao.csv"],
    "Processamento":   ["ProcessaViniferas.csv", "ProcessaAmericanas.csv", "ProcessaMesa.csv", "ProcessaSemclass.csv"],
    "Comercialização": ["Comercio.csv"],
    "Importação":      ["ImpVinhos.csv", "ImpEspumantes.csv", "ImpFrescas.csv", "ImpPassas.csv", "ImpSuco.csv"],
    "Exportação":      ["ExpVinho.csv", "ExpEspumantes.csv", "ExpUva.csv", "ExpUva.csv"]
}

def scrap_and_find_links(aba):

    # Verifica se a aba informada existe no dicionário
    if aba in embrapa:
        linkParaAba = embrapa[aba]
    else:

    # Se aba não estiver presente, imprime uma mensagem de aviso
        return f"Nenhuma busca foi encontrada para '{aba}' "

    #faz o scraping do site especificado.
    website_content = scrap_website(servidor_ftp)

    #verifica se há conteúdo no site
    if not website_content:
        #lança uma exceção
        raise HTTPException(status_code=404, detail='nenhum conteúdo encontrado')

    #extrai os links do conteúdo da pagina no primeiro nivel
    links = find_links_at_level_one(website_content, linkParaAba)

    #verifica se tem link extraidos
    if not links:
        print(f"DEBUG {links}")
        raise HTTPException(status_code=404, detail='nenhum conteúdo encontrado')

    #retorna o link contraido com resposta
    return {'links': links}