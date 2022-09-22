# Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que 
# tuplas são imutáveis enquanto listas são mutaveis. Podemos criar tuplas através da classe
# tuple, ou colocando valores separados por vírgula de parenteses.

frutas = ('laranja','pera','uva')

letras = tuple('python')

numeros = tuple([1,2,3,4])

pais = ('Brasil')

matriz = (
    (1 ,'a', 2),
    ('b', 3, 4),
    (6, 5, 'c')
)

matriz[0] # (1, 'a', 2)
matriz[0][0] # 1
matriz[0][-1] # 2