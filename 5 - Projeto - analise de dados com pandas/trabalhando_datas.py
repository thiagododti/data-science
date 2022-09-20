import pandas as pd

#leitura de arquivos

df1 = pd.read_excel("base_de_dados/Aracaju.xlsx")
df2 = pd.read_excel("base_de_dados/Fortaleza.xlsx")
df3 = pd.read_excel("base_de_dados/Natal.xlsx")
df4 = pd.read_excel("base_de_dados/Recife.xlsx")
df5 = pd.read_excel("base_de_dados/Salvador.xlsx")

# juntando todos os arquivos

df = pd.concat([df1,df2,df3,df4,df5])

df['Receita'] = df['Vendas'].mul(df['Qtde'])


# Transformando a coluna de data em tipo inteiro

df['Data'] = df['Data'].astype('int64')

# verificando o tipoe de dado de cada coluna

df.dtypes

# Transformando a coluna de data em data

df['Data'] = pd.to_datetime(df['Data'])

# agrupando por ano

df.groupby(df['Data'].dt.year)['Receita'].sum()

# criando uma nova coluna com ano

df['Ano_Venda'] = df ['Data'].dt.year

# extraindo mes e dia

df['Mes_Venda'], df['Dia_Venda'] = (df['Data'].dt.month, df['Data'].dt.day)

# Retornando a data mais antiga

df['Data'].min()

# Calculando a diferença de dias

df['Diferenca_Dias'] = df['Data'] - df['Data'].min()

# criando coluna de trimestre

df['Trimestre_Venda'] = df['Data'].dt.quarter

# filtrando as vendas de 2019 do mes de março

vendas_marco_19 = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]

print(vendas_marco_19)

