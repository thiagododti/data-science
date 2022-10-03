# Utilizando a biblioteca Scikit learn

# Esta biblioteca dispõe de ferramentas simples e eficientes para análise preditiva
# de dados, é reutilizável em diferentes situações, possui código aberto, sendo
# acessóvel a todos e foi construída sobre os pacotes NumPy, SciPy, e matplotilib.


# exemplo

# Neste exemplo iremos criar uma massa de dados com 200 observações, com apenas uma
# variável preditora, que será a variável x e a variável target, que será a y. Para isso
# indicamos os parâmetros n_samples = 200 e n_features = 1. O parâmetro noise define o
# quão dispersos os dados estarão um dos outros.

from sklearn.datasets import make_regression

#gerando uma massa de dados:

x,y = make_regression(n_samples=200, n_features=1, noise=30)

# Utilizaremos o pacote matplotlib, como módulo pyplot e a função scatter(), que criará o
# gráfico, e função show() que o exibirá na tela.

import matplotlib.pyplot as plt

# mostrando no gráfico:

plt.scatter(x,y)
plt.show()

# Com os dados gerados, já podemos iniciar a crianção de nosso modelo de machine learning.
# Para isso utilizaremos o módulo linear_model, e a função LinearRegression().

from sklearn.linear_model import LinearRegression

# Criação do modelo

modelo = LinearRegression()