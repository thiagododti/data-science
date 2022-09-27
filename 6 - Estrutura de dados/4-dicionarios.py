# Dicionários

# Um dicionário é um conjunto não-ordenado e pares
# chave:valor, onde as chaves são únicas em uma dada instância
# do dicionário. Dicionários são delimitados por chaves: {}, e
# contém uma lista de pares chave:valor separada por vírgulas.

# Estrutura

pessoa = {
    "nome": "Thiago",
    "idade": 30
}

pessoa = dict(nome="Thiago", idade=30)

pessoa["telefone"] = "98125-7064"

print(pessoa)  # {'nome': 'Thiago', 'idade': 30, 'telefone': '98125-7064'}


# Acessar os valores

print(pessoa["nome"])  # Thiago
print(pessoa["idade"])  # 30

#########################################################################

# Dicionário aninhados

# Dicionários podem armazenar qualquer tipo de objeto Python
# como valor, desde que a chave para esse valor seja um objeto
# imutável como (strings e números)

contatos = {
    "thiago@thiago.com.br": {"nome": "Thiago", "telefone": "3333-4444"},
    "lucas@lucas.com.br": {"nome": "Lucas", "telefone": "4444-5555"},
    "luisa@luisa.com.br": {"nome": "Luisa", "telefone": "6666-7777"}
}

print(contatos["luisa@luisa.com.br"]["nome"])

#########################################################################

# iterar dicionários

# A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

#########################################################################

# METODOS DICIONÁRIOS

# {}.clear() - Limpa o dicionário

contatos.clear()

# {}.copy() - tira uma copia do dicionário
contatos = {
    "thiago@thiago.com.br": {"nome": "Thiago", "telefone": "3333-4444"},
    "lucas@lucas.com.br": {"nome": "Lucas", "telefone": "4444-5555"},
    "luisa@luisa.com.br": {"nome": "Luisa", "telefone": "6666-7777"}
}


copia = contatos.copy()

# {}.fromkeys([]) - ele cria chaves no dicionario com valores vazios

# - as chaves serão criadas com valores nulos
dict.fromkeys(["nome", "telefone"])

# as chaves serão criadas com o valor padrão "vazio" definido
dict.fromkeys(["nome", "telefone"], "vazio")

# {}.get() - acessa valores dentro do dicionário

print(contatos.get("chave"))  # none
print(contatos.get("chave", {}))  # {}
print(contatos.get("thiago@thiago.com.br", {}))

# {}.items() - retorna tuplas

# dict_items([('thiago@thiago.com.br', {'nome': 'Thiago', 'telefone': '3333-4444'}), ('lucas@lucas.com.br', {'nome': 'Lucas', 'telefone': '4444-5555'}), ('luisa@luisa.com.br', {'nome': 'Luisa', 'telefone': '6666-7777'})])
print(contatos.items())

# {}.keys() - retorna somente as chaves do dicionário

# dict_keys(['thiago@thiago.com.br', 'lucas@lucas.com.br', 'luisa@luisa.com.br'])
print(contatos.keys())

# {}.pop() - ele remove e retorna o valor que ele removeu.

contatos.pop("lucas@lucas.com.br")

# {}.popitem() - ele remove os items na sequencia sem passar argumento e retorna erro caso nao tenha mais nenhum item

contatos.popitem()

# {}.setdefault - se o atributo nao existir ele acrescenta ao dicionario

print(contatos)
contatos.setdefault("idade", "28")
print(contatos)


# {}.update() - atualiza um dicionario com outro dicionario

contatos.update({"thiago@thiago.com.br": {"nome": "Thi"}})

print(contatos)

# {}.values - retorna todos os valores que estao no dicionarios

contatos.values()

# in - metodo para verificar se uma chave existe

contatos = {
    "thiago@thiago.com.br": {"nome": "Thiago", "telefone": "3333-4444"},
    "lucas@lucas.com.br": {"nome": "Lucas", "telefone": "4444-5555"},
    "luisa@luisa.com.br": {"nome": "Luisa", "telefone": "6666-7777"}
}

# - verifico que o valor é uma chave do dicionario
resultado = "thiago@thiago.com.br" in contatos
print(resultado)

# - verifico se tem idade no dicionario interno.
resultado = "idade" in contatos["thiago@thiago.com.br"]
print(resultado)

# del - voce passa o objeto que quer remover do dicionario

del contatos["thiago@thiago.com.br"]["telefone"]
print(contatos["thiago@thiago.com.br"])  # {'nome': 'Thiago'}
