#Módulos
from functools import reduce

dados = [2, 3, 4 ,5]

#Para utilizar o redue() nós precisamos de uma função que receba dois parametros
multi = lambda x, y: x * y

'''O que o programa vai fazer é:
Pega no primeiro valor e multiplica pelo segundo valor da lista,
depois pega nesse resultado e multiplica pelo número que vem a seguir 
na lista, depois pega nesse resultado e multiplica pelo número que vem a seguir ...

2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
'''
res = reduce(multi, dados)
print(res)

#Neste caso em especifico é preferivel fazer como está a seguir
a = 1
for n in dados:
    a = a * n
print(a)