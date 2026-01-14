from fastapi import FastAPI
from fastapi.responses import FileResponse
from variaveis.variaveis import var_pathClientesJSON
import uvicorn
import os

app = FastAPI()

@app.get("/v1/marketing/{nomeArquivo}")
def retorno_dados_marketing(nomeArquivo: str):
    """
    Retorna o arquivo dos leads.
    
    :param arquivo: arquivo.json que contém os dados dos leads
    """
    var_objArquivoJSON = os.path.join(var_pathClientesJSON, f"{nomeArquivo}.json")
    return FileResponse(
         path = var_objArquivoJSON
       , media_type = "application/json"
       , filename = f"{nomeArquivo}.json"  
    )

@app.get("/v1/crm/{nomeArquivo}")
def retorno_dados_crm(nomeArquivo : str):
    """
    Retorna os arquivos vendas e clientes que são dados do comercial.
    
    :param nomeArquivo: 
    """
    var_objArquivoJSON = os.path.join(var_pathClientesJSON, f"{nomeArquivo}.json")
    return FileResponse(
         path = var_objArquivoJSON
       , media_type = "application/json"
       , filename = f"{nomeArquivo}.json"  
    )