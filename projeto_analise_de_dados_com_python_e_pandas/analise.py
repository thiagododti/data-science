# importando biblioteca pandas
import pandas as pd

df = pd.read_csv('base_de_dados/Gapminder.csv',error_bad_lines=False,sep=";")

# Visualizando as 5 primeiras linhas

df.head()

# trocando o nome das colunas

df = df.rename(columns={"country":"pais","continent":"continente","year":"ano","lifeExp":"expectativa de vida","pop":"populacao","gdpPercap":"pib"})

# retorno da quantidade de linhas e colunas

df.shape # primeiro valor é o numero de linhas o segundo é o numero de colunas

# retornar somente o nome das colunas.

df.columns # Index(['pais', 'continente', 'ano', 'expectativa de vida', 'populacao', 'pib'], dtype='object')

# descobrir o tipo de dados de cada coluna

df.dtypes

#pais                    object
#continente              object
#ano                      int64
#expectativa de vida    float64
#populacao                int64
#pib                    float64


#vizualizar as ultimas linhas

df.tail(15)

#vizualizar estatisticas de dados

df.describe()

# descobrindo os continentes que tem na base sem

df['continente'].unique()

# realizando filtros na base de dados

Oceania = df.loc[df["continente"] == "Oceania"] # armazenando todas as linhas nas quais possui oceania como continente

# agrupamento de dados

df.groupby("continente")["pais"].nunique() #agrupamento pela coluna continentes contando quantos continenetes possui individualmente

df.groupby("ano")["expectativa de vida"].mean() #agrupamento por ano calculando a media da expectativa de vida por ano

df["PIB"].sum() # somando a coluna pib

