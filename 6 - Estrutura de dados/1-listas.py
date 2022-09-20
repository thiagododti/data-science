# Listas em python podem armazenar de maneira sequencia
# qualquer tipo de objeto. Podemos criar listas utilizando
# o construtor list, a função range ou colocando valores
# separados por virgula dentro de colchetes. Listas
# são objetos mutáveis, portanto podemos alterar seus valores
# após a criação.

frutas = ['laranja', 'maca', 'uva']

vazia = []

letras = list('python')

numeros = list(range(10))

carro = ['ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]

# indice da lista sempre inicia em 0, 1, 2, 3 e etc

print(frutas[1])  # maca

# sequencias suportam indices negativos

print(frutas[-1])  # uva

print(frutas[-2])  # maca

#################################################################

# lista aninhada

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0][1])  # 3
print(matriz[-1][-1])  # c

#################################################################

# Fatiamento

# alem de acessar elementos diretamente, podemos extrair um conjunto
# de valores de uma sequência. Para isso basta passar o índice inicial
# e/ou final para acessar o conjunto. Podemos ainda informar quantas
# posições o curso deve "Pular" no acesso.

lista = ['p','y','t','h','o','n']

print(lista[2:])    # ['t', 'h', 'o', 'n']
print(lista[:2])    # ['p', 'y']
print(lista[1:3])   # ['y', 't']
print(lista[0:3:2]) # ['p', 't']
print(lista[::])    # ['p', 'y', 't', 'h', 'o', 'n']
print(lista[::-1])  # ['n', 'o', 'h', 't', 'y', 'p']

#################################################################

# Iterar lista

# a forma mais comum para percorrer os dados de uma lista e utilizando o comando for.

carros = ['gol','celta','palio']

for carro in carros:
    print(carro)

#################################################################

# função enumerate

#as vezes é necessário saber qual o índice do objeto dentro do laço for.
# Para isso podemos usar a função enumerate.

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#################################################################

# Compreensão de listas

# A compreensão de lista oferece uma sintaxe mais curta quando você
# deseja: criar uma nova lista com base nos valores de uma lista
# existente (filtro) ou gerar uma nova lista aplicando alguma
# modificação nos elementos de uma lista existente.

numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# filtro versão 2

pares = [numero for numero in numeros if numero % 2 == 0]

# modificando valores versão 1

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# modificando valores versão 2

quadrado = [numero ** 2 for numero in numeros]