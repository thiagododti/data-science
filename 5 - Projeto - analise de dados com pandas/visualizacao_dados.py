import pandas as pd

# leitura de arquivos

df1 = pd.read_excel("base_de_dados/Aracaju.xlsx")
df2 = pd.read_excel("base_de_dados/Fortaleza.xlsx")
df3 = pd.read_excel("base_de_dados/Natal.xlsx")
df4 = pd.read_excel("base_de_dados/Recife.xlsx")
df5 = pd.read_excel("base_de_dados/Salvador.xlsx")

# juntando todos os arquivos

df = pd.concat([df1, df2, df3, df4, df5])

df['Receita'] = df['Vendas'].mul(df['Qtde'])

df['LojaID'].value_counts(ascending=False)

# grafico de barras vertical

df['LojaID'].value_counts().plot.bar()

# grafico de barras horizontal

df['LojaID'].value_counts(ascending=True).plot.barh()

# Gráfico de pizza

df.groupby(df['Data'].dt.year)['Receita'].sum().plot.pie()

# Total de vendas por cidade

df['Cidade'].value_counts()

# adicionando um titulo e alterando o nome dos eixos

import matplotlib.pyplot as plt

df['Cidade'].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

