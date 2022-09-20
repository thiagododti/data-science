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
