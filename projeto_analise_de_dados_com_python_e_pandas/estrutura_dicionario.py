# DICIONARIOS

# para criar um dicionário utilizamo as {}

dc = {"maçã":20, "Banana":10, "Laranja":15, "Uva":5} #dicionário trabalha com chave e valor

# lendo um dicionario

print(dc)

# acessando o valor de um dicionario atraves de chave

print(dc["maçã"])

# atualizando o valor da maçã

dc["maçã"] = 25

# retornando todas as chaves do dicionário

print(dc.keys())

# retornando todos os valores do dicionário

print(dc.values())

# verificando se já existe uma chave no dicinário e caso nao exista ele insere

dc.setdefault("Limão", 22)

