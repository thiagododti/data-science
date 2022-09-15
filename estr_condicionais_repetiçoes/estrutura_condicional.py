saldo = 2000.0

conta_normal = True
conta_universitaria = False
saque = 500

cheque_especial = 450

saque = float(input("Informe o valor do saque: "))

#if

if saldo >= saque:
    print("Realizando o saque")

if saldo < saque:
    print("Saldo insuficiente!")

#######################################################

#if else

if saldo >= saque:
    print("Realizando o saque!")
else:
    print("Saldo insuficiente!")

#######################################################

#if elif else

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    saque = float(input("Informe o valor do saque: "))
elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    print("Opção inválida")

#######################################################

#if aninhado

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")

#######################################################

#if ternario

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")