#Entrada
#O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na 
# viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

#Saída
#Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split()

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal

AUTONOMIA = 12 #12 litros por km

NECESSARIO = (int(valores[1])*int(valores[0]))/AUTONOMIA

print(f"{NECESSARIO:.3f}")