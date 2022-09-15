# lista
animais = ["cachorro","gato","rato"]

print(animais[0]) #imprimindo o primeiro animal da lista

# substituir um elemento da lista

animais[0] = "papagaio"

# remover um elemento da lista

animais.remove("gato")

# retornar o tamanho da lista

len(animais) # 2

# verificar um objeto dentro da lista

"rato" in animais # true

#####################

lista = [500,30,300,80,10]

# verificar o maior numero da lista

max(lista) # 500

# verificar o menor numero da lista

min(lista) # 10

# adicionar um elemento a lista

animais.append("leao")

# adicionar uma lista aninhada

animais.append(["periquito", "aguia"]) # ['papagaio', 'rato', 'leao', ['periquito', 'aguia']]

# adicionar mais de um elemento na lista

animais.extend(["giraffa", "cobra"]) # ['papagaio', 'rato', 'leao', ['periquito', 'aguia'], 'giraffa', 'cobra']

print(animais)

# contar quantos elementos iguais tem na lista

animais.count("cobra")

# ordenar a lista do menor para o maior

lista.sort()

