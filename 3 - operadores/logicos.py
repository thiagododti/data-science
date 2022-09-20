saldo = 1000
saque = 200
limite = 100

#operador E ( and )
saldo >= saque and saque <= limite
#false

#quando as duas preposiçoes forem verdadeiras o operador and terá como resultado true
########################################################################################

#operador OU ( or )
saldo >= saque or saque <= limite
#true

#quando pelo menos uma preposição for verdadeira o perador or terá como resultado true
########################################################################################

#operador de negação

not 1000 > 1500

#o perador not pega o resultado da primeira comparação e inverte o resultado
# é falso que 1000 é maior que 1500 e assim eu nego com operador not logo a preposição se torna true

########################################################################################

#em casos com expressões, segue a ordem matematica com relaçao aos parentereses

r = (2>1 and 2>1) or (2<1 and 2>1) #r true