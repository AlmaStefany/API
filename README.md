## Windowns:
1. Criando um ambiente virtual:
```bash
py -m venv venv 
``` 
2. Ativando ambiente virtual:
```bash
venv\Scripts\activate
```
3. Instalando requirements
```bash
pip install -r requirements.txt 
```

## Ativando Servidor Web
3. Instalando requirements
```bash
uvicorn main:app --reload
```

## Comandos utils
```bash
# Verificar o Caminho do Python
Get-Command python

# Verificar pacotes instalados
pip list

# Reinstalar os Pacotes 
pip install --upgrade --force-reinstall fastapi selenium
```