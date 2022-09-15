# Em python exite 3 formas de interpolar variáveis em strings
#   1 - usando o sinal de %
#   2 - usando metodo format
#   3 - utilizando f strings

# a primeira nao é atualmente recomendada e o uso é raro em python 3

# %

nome = "Thiago"
idade = 28
profissao = "Programador"
linguagem = "Python"

print ("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome,idade,profissao,linguagem))

# format

print ("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome,idade,profissao,linguagem))

#f-string

print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# formatar com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") #   "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}") # "Valor de PI:          3.14"



