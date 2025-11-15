🎬 Projeto Extrator de Filmes Populares (TMDb)
Este projeto é um script simples em Python para extrair dados de filmes populares da API do The Movie Database (TMDb) e salvar os resultados em um arquivo CSV (.csv) para análise posterior.

✨ Funcionalidades
Faz requisições HTTP para a API v3 do TMDb.

Extrai a lista de filmes populares (/movie/popular).

Converte os dados JSON retornados em um DataFrame do Pandas.

Salva o DataFrame em um arquivo filmes_populares.csv.

🛠️ Tecnologias Utilizadas
Python (3.13)

requests: Para fazer as requisições HTTP.

pandas: Para manipulação e estruturação dos dados (DataFrame).

openpyxl: Motor necessário para o Pandas salvar no formato CSV (.csv).
