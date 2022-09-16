import pandas as pd

#leitura de arquivos

df1 = pd.read_excel("base_de_dados/Aracaju.xlsx")
df2 = pd.read_excel("base_de_dados/Fortaleza.xlsx")
df3 = pd.read_excel("base_de_dados/Natal.xlsx")
df4 = pd.read_excel("base_de_dados/Recife.xlsx")
df5 = pd.read_excel("base_de_dados/Salvador.xlsx")

# juntando todos os arquivos

df = pd.concat([df1,df2,df3,df4,df5])

# substituindo valores nulos por zero

df["Vendas"].fillna(0,inplace=True)

# criando a coluna receita

df['Receita'] = df['Vendas'].mul(df['Qtde'])

df.head()

# retornando a maior receita

df['Receita'].max()

# retornando a menor receita

df['Receita'].min()

# retornando rankings - Top 3

df.nlargest(3, 'Receita')

# retornando rankins - Last 3

df.nsmallest(3, 'Receita')

# agrupamento por cidade

df.groupby('Cidade')['Receita'].sum()

# ordenando o conjunto de dados

df.sort_values('Receita',ascending=False).head(10)