 # DataFrame

 # Agora se visualizarmos novamente os primeiros 4 dados do nosso conjunto,
 # veremos que todos os valores passados para na_values, além dos próprios dados
 # ausentes, foram substituídos por NaN.

df.head(n=4)

##################################################################################

# df.shape

# retorna a quantidade de linhas e colunas que o dataframe possui

df.shape

##################################################################################

# df.info()

# Já para saber que formado se encontram os dados em cada coluna, além da quantidade
# de memória para ler esse conjunto de dados, podemos utilizar o comando info.

df.info()

##################################################################################

# Alterações

# Na sequência, podemos visualizar quais são nossas colunas existentes e até mesmo
# alterar esses nomes, basta passar o novo conjunto de nomes desejados com a mesma
# quantidade de colunas existente no conjunto original>

df.columns

index(['id', 'data_aq', 'produto', 'quantidade', 'valor UN', 'total' , 'setor'], dtype='object')

df.columns = ['id','data_aq','produto','quantidade','valor_un','valor_total','setor']

##################################################################################

# Verificação

# Para verificar quantos dados faltantes existem em nosso conjunto

df.isnull().sum() # procura nulos e depois soma a quantidade de valores identificados.

##################################################################################

# Valores únicos

# No nosso objeto serie podemos verificar quais os valores únicos existem naquela
# coluna, com o método unique

df['setor'].unique()

##################################################################################

# Agrupamentos

# Ainda a partir desse método podemos gerar uma visualização simples e rápida com
# resultado. Como? com o método plot.

df['setor'].value_counts().plot(kind='bar')

##################################################################################

# Dados estatísticos

# o Pandas colabora na exibição de algumas informações estatísticas a respeito do 
# nosso conjunto de dados e permite que possamos realizar facilmente uma análise
# com nosso objeto DataFrame

df.describe()