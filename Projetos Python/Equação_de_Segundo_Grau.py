#Realizar equação de segundo grau

#Módulos
import math

#Texto com a equação
print("A equação é ax^2 + bx + c")
print("..............................")

#Valores
a = int(input("Introduz o valor de a: "))
b = int(input("Introduz o valor de b: "))
c = int(input("Introduz o valor de c: "))

#Conta
d = (b*b) - 4*a*c

#Comprovar os valores
if d < 0:
    print('Não existe solução real')
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)

#Imprimir as soluções
print("----------Soluções----------\nSolução de x1: ", x1, "\nSolução de x2:", x2)

#Imprimir as soluções arredondadas
print("----------Soluções Aredondadas----------")
print("Solução de x1: ", "{:.2f}".format(x1))
print("Solução de x2: ", "{:.2f}".format(x2))