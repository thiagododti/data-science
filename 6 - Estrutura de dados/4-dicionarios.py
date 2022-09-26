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

#iterar dicionários

# A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave,valor)