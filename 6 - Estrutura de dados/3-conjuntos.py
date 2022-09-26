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

# {}.union - une os dois conjuntos, mas elimina a duplicidade

conjunto_a = set([1, 2, 3])
conjunto_b = set([2, 3, 4])

conjunto = conjunto_a.union(conjunto_b)  # {1, 2, 3, 4}

# {}.intersection - une o conjunto somente com valores que existem nos 2

print(conjunto)

conjunto2 = conjunto_a.intersection(conjunto_b)  # {2, 3}

print(conjunto2)

# {}.difference - pega a diferença de um conjunto comparada com outro

conjuntoA = conjunto_a.difference(conjunto_b)  # {1}
conjuntoB = conjunto_b.difference(conjunto_a)  # {4}

# {}.symmetric_difference - pega a diferença que existe nos dois grupos

conjuntosDif = conjunto_a.symmetric_difference(conjunto_b)  # {1, 4}

# {}.issubset - Verifica se todos os valores de um conjunto existe em um conjunto passado como parametro

conjunto_c = set([4, 1, 2, 5, 6, 3])

conjunto_a.issubset(conjunto_c)  # True
conjunto_c.issubset(conjunto_a)  # False

# {}.issuperset - verifica se os valores do conjunto passado como parametro existem dentro do conjunto solicitado para verificação

conjunto_a.issubset(conjunto_c)  # False
conjunto_c.issubset(conjunto_a)  # True

# {}.isdisjoint - verifica nao existem valores em comum entre os conjuntos.

conjunto_a.isdisjoint(conjunto_b) # False

# {}.add - se o elemento nao existe, ele é adicionado ao conjunto

sorteio = set([1,23])

sorteio.add(25) # {1, 23, 25}

# {}.clear - limpa todos os itens do conjunto

sorteio.clear() # {}

# {}.copy - copia o conjunto.

sorteio.copy()

# {}.discard() - elimina um valor passado por parametro do conjunto

sorteio.add([1,2,3,4,5,6])
sorteio.discard(1) # {2,3,4,5,6}

# {}.pop - elimina o primeiro valor do conjunto

sorteio.pop() #{3,4,5,6}
sorteio.pop() #{4,5,6}

# {}.remove - elimina o valor passado como parametro, mas ele faz a verificação de erro caso o valor nao exista

sorteio.remove(4) # {5,6}
sorteio.remove(10) # erro

# len() - conta quantos elementos existem no conjunto

len(sorteio) # 2

# in verifica se existe um valor dentro do conjunto

1 in sorteio # False
5 in sorteio # True

