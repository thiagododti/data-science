# [].append - adicionar um novo elemento na lista

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, 'Python', [40, 30, 20]]

####################################################################

# [].clear - limpar uma lista

lista.clear()

print(lista)  # []

####################################################################

# [].COPY - copio toda a lista para uma variavel diferente. o que eu alterar na variavel que foi copiada nao reflete na lista original

lista = [1, 'Python', [40, 30, 20]]

lista2 = lista.copy()

print(lista2)  # [1, 'Python', [40, 30, 20]]

####################################################################

# [].count conta quantas vezes um determinado valor repete na lista

numeros = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 10, 10, 10, ]

numeros.count(3)  # 2
numeros.count(6)  # 3
numeros.count(10)  # 4

####################################################################

# [].extend - acrescenta variaos itens na lista de uma vez ( não adiciona lista aninhada)

linguagens = ['python', 'js', 'c']

linguagens.extend(['java', 'csharp'])

print(linguagens)  # ['python','js','c','java','csharp']

####################################################################

# [].index - descobre qual o indice da primeira ocorrencia do objeto

linguagens.index('java')  # [3]
linguagens.index('python')  # [0]

####################################################################

# [].pop - retira o ultimo elemento adicionado na lista

linguagens.pop() # removeu csharp
linguagens.pop(0) # removeu python

####################################################################

# [].remove

linguagens.remove('c') # remove o indice pelo valor passado

####################################################################

# [].reverse - ele pega a lista e coloca ao contrario todos os valores

linguagens.reverse() 

####################################################################

#[].sort - ele ordena a lista em ordem alfabetica ou numerica

letras = ['a','b','z','g','t','p','m','s']

print(letras)

letras.sort() # ordena em ordem crescente
letras.sort(reverse=true) #ordena em ordem descescente

print(letras)

#[].len - informa a quantidade de objetos dentro de uma lista

len(letras) # 8

# [].sorted - mesma coisa do sort mas a diferença é que o sorted é uma função

sorted(letras, key=lambda x: len(x))
