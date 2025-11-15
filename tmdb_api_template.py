# Projeto de ETL Simples com API Pública de Filmes
# Extração de Dados usando requests

import requests
import json #para formatar a saída

# URL do endpoint da API
url = 'https://api.themoviedb.org/3/movie/popular?api_key=CHAVE-DA-API-AQUI'

# Obter a resposta
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    print('Requisição bem-sucedida!')
    data = response.json()
else:
    print(f'Falha na requisição:{response.status_code}' )

# Acessando a lista de filmes populares
lista_de_filmes = data.get('results', [])

# Converter a lista de filmes em um dataframe

import pandas as pd

if lista_de_filmes:
    df = pd.DataFrame(lista_de_filmes)
    # Exibir os primeiros 5 resultados
    print('\n---DataFrame Criado---\n')
    print(df.head())

# Limpeza e Transformação de dados

# Encontrar filmes com nota média acima de 7.5
filmes_populares_excelentes = df[df['vote_average'] > 7.5]
print('\n---Filmes com Nota Média Acima de 7.5---\n')
print(filmes_populares_excelentes[['title', 'vote_average']].head())

# Listar todas as colunas do DataFrame
colunas = df.columns
#print(colunas)

# Converter a data de lançamento para o formato datetime
df['release_date'] = pd.to_datetime(df['release_date'])
data_de_lancamento = df['release_date']
#print(data_de_lancamento.head())

# Visualização de dados

import matplotlib.pyplot as plt

# Histograma das notas médias dos filmes
plt.figure(figsize=(10,6))
plt.hist(df['vote_average'], bins=10, edgecolor='black')
plt.title('Distribuição das Notas Médias dos Filmes Populares')
plt.xlabel('Nota Média')
plt.ylabel('Frequencia')
plt.grid(axis='y', alpha=0.5)
plt.show()

# Salvar o DataFrame limpo em um arquivo CSV
df.to_csv('filmes_populares.csv', index=False)