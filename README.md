API Local – Projeto de Demonstração (Kurier 2026)
Visão Geral
Este projeto consiste em uma API Local desenvolvida em Python utilizando FastAPI, criada para simular a disponibilização de dados de sistemas distintos (Marketing e CRM) para consumo por um processo de ETL.
A API fornece arquivos JSON por meio de endpoints REST, representando um cenário real de integração entre sistemas, muito comum em arquiteturas orientadas a dados.
Este projeto faz parte de um desafio técnico para a vaga de Desenvolvedor Pleno.

Objetivo
- Disponibilizar dados em formato JSON via API
- Simular fontes de dados de diferentes domínios de negócio
- Servir como origem de dados para um processo de ETL
- Facilitar testes, auditoria e validação de dados

Estrutura da Solução
A estrutura da API foi pensada para manter simplicidade, organização e clareza, separando configuração, dados e execução da aplicação.
PROJETO_KURIER_2026_API
│
├── repositorio/
│   └── *.json
│
├── variaveis/
│   └── variaveis.py
│
├── index.py
├── KUR_API.bat
├── requirements.txt
├── README.md
├── .gitignore
└── venv/

repositorio/
- Diretório responsável por armazenar os arquivos JSON disponibilizados pela API.
- Contém os dados utilizados no desafio técnico
- Atua como fonte de dados simulada
- Os arquivos deste diretório são retornados diretamente pelas rotas da API

variaveis/
- Camada de variáveis globais e configurações da aplicação.
- Centraliza parâmetros reutilizáveis
- Evita valores fixos no código
Exemplo:
Caminho base dos arquivos JSON (var_pathClientesJSON)

index.py
- Arquivo principal da aplicação.
- Responsável por:
	Inicializar a aplicação FastAPI
- Definir as rotas da API
- Retornar arquivos JSON via HTTP utilizando FileResponse

KUR_API.bat
- Script para inicialização da API localmente.
- Automatiza a execução do servidor Uvicorn
- Facilita o uso em ambientes de avaliação e testes

Outros Arquivos
- requirements.txt: dependências do projeto
- .gitignore: controle de versionamento
- README.md: documentação
