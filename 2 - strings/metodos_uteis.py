# METODOS UTEIS DA CLASSE STRING

#manipulaçao de letras

curso1 = "pYtHoN"

print(curso1.upper())    #"PYTHON" - tudo maiusculo

print(curso1.lower())    #"python" - tudo minusculo

print(curso1.title())    #"Python" - primeira letra em maiusculo

#########################################################################################
#manipulação de espaços

curso2 = "       Python  "

print(curso2.strip())   #"Python"       -elimina todos os espaços em branco

print(curso2.lstrip())  #"Python  "     -elimina os espaços em branco da esquerda

print(curso2.rstrip())  #"   Python"    -elimina os espaços em branco da direita

#########################################################################################
#junção e centralização

curso3 = "Python"

print(curso3.center(10, "#"))    # "##Python##" - informa que deseja que a string tenha 10 caracteres e que os caracteres adicionais sejam #

print(".".join(curso3)) # "P.y.t.h.o.n" - cada letra que o join passar ele vai inserir um caractere informado na string

#########################################################################################
