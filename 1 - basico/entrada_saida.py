print('Hello World')

nome = 'Thiago'
print(f"meu nome e {nome}") #f seguido das aspas sinaliza que vai ser inseridas variaveis dentro do print

##################
#FUNÇÃO input

nome = input("Digite o nome: ") #o valor digitado será armazenado dentro da variavel nome
sobrenome = input("Digite o sobrenome: ")

print(nome, sobrenome) #o valor que foi armazenado é exibido pela função print
print(nome, sobrenome, end="...\n") #end adiciona a terminação desejada
print(nome, sobrenome, sep="#") #sep eu troco o separador que por padrão vem o espaço
print(f"nome: {nome}, sobrenome: {sobrenome}") #f seguido de aspas eu insiro a variavel dentro do texto

