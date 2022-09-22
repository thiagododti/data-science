# Criando Sets

# pode definir um conjunto atraves da função set

# um set é uma coelção que não possui objetos repetidos,
# usamos sets para representar conjuntos matemáticos ou
# eliminar itens duplicados de um iterável

numeros = set([1, 2, 3, 1, 3, 4])  # {1,2,3,4}

# {'b', 'a', 'x', 'i', 'c'} - o set nao tras os objetos na ordem.
abacaxi = {"abacaxi"}

carros = set(("palio", "gol", "celta", "palio"))  # {"gol", "celta", "palio"}

print(abacaxi)

# Conjuntos em python não suportam indexação e nem fatiamento,
# caso queira acessar os seus valores é necessário
# converter o conjunto para lista.

numeros = list(numeros)

print(numeros[0])  # 1

# a forma mais comum para percorrer os dados de um conjunto
# é utilizando o comando for.

for carro in carros:
    print(carro)

# Às vezes é necessário saber qual  o índice do objeto dentro do
# laço for. Para isso podemos usar a função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#######################################################################################

# METODOS SET

# {}.union

conjunto_a = set([1, 2])
conjunto_b = set([3, 4])

conjunto = conjunto_a.union(conjunto_b)

print(conjunto)

# {}.
