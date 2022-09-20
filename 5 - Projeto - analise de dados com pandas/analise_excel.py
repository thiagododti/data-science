import pandas as pd

#leitura de arquivos

df1 = pd.read_excel("base_de_dados/Aracaju.xlsx")
df2 = pd.read_excel("base_de_dados/Fortaleza.xlsx")
df3 = pd.read_excel("base_de_dados/Natal.xlsx")
df4 = pd.read_excel("base_de_dados/Recife.xlsx")
df5 = pd.read_excel("base_de_dados/Salvador.xlsx")

# juntando todos os arquivos

df = pd.concat([df1,df2,df3,df4,df5])

# exibindo as 5 primeiras linhas

df.head()

# exibindo as 5 ultimas linhas

df.tail()

# pegando uma amostra

df.sample(5)

# verificando o tpo de dado de cada coluna

df.dtypes()

# alterando o tipo de dado da coluna LojaID

df["LojaID"] = df["LojaID"].astype("object")

# consultando linhas com valores nulos

df.isnull().sum() # trazendo a soma de valores nulos de cada coluna.

# substituindo os valores nulos pela média

df["Vendas"].fillna(df["Vendas"].mean(), inplace=True) #inplace aciona para troca-lo em memoria.

df["Vendas"].mean()

# substituindo valores nulos por zero

df["Vendas"].fillna(0,inplace=True)

# apagando linhas com valores nulos

df.dropna(inplace=True)

# apagando as linhas com valores nulos com base apenas em 1 coluna

df.dropna(subset=['Vendas'],inplace=True)

# Removendo linahs que estejam com valores faltanres em todas as colunas

df.dropna(how="all", inplace=True)

