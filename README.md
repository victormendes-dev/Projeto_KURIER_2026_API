API de Dados CSV – Processo Seletivo Kurier
Descrição:

Esta é uma API desenvolvida em Python utilizando FastAPI, construída como parte do processo seletivo para desenvolvedor pleno na Kurier. 
A API tem como objetivo disponibilizar dados de arquivos CSV de forma estruturada e acessível via rotas REST, permitindo fácil integração com sistemas e ferramentas de análise.

A aplicação permite:
- Listar arquivos CSV disponíveis.
- Consultar dados específicos de um CSV em formato JSON.
- Facilitar consultas de dados sem necessidade de abrir diretamente os arquivos.

Funcionalidades:
- Listar arquivos CSV
Rota: /files
Retorna a lista de todos os arquivos CSV disponíveis no diretório configurado.

Visualizar conteúdo de um CSV:
Rota: /files/{filename}
Retorna o conteúdo do CSV em formato JSON, permitindo fácil integração com front-ends ou sistemas de análise de dados.

Tecnologias Utilizadas:
- Python 3.11+
- FastAPI – para desenvolvimento da API.
- Uvicorn – servidor ASGI para rodar a aplicação.

documentação da API:
- http://127.0.0.1:8000/docs
