#for

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("For else executa ao finalizar toda a repetição do for")

print()
####################################################################
# range()

# e uma função built-in do python. Ela e usada para produzir uma sequencia de numeros inteiros a partir 
# de um inicio exclusivo para fim exclusivo

#recebe 3 argumentos: stop(obrigatorio), start(opcional) e step(opcional)

list(range(4))
#[0,1,2,3]

####################################################################

#range com for

for numero in range(0,11):
    print(numero, end=" ")

# 0 1 2 3 4 5 6 7 8 9 10

#tabuada do 5

for numero in range(0,51,5):
    print(numero, end=" ")
# 0 5 10 15 20 25 30 35 40 45 50

####################################################################

#while

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o extrato ...")
else:
    print("Else no while também executa ao final do while")

####################################################################

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        #break # para quando alcançar essa condição
        #continue #pula quando essa condição for atingida
        break

    print(numero)