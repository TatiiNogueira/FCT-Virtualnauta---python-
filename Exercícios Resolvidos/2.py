#Crie uma função que retorne o valor da expressão:
#2/3 + 3/5 + 4/7 + 5/9 + … + n/m,
#para um valor de n definido pelo usuário.
#Verifique se o valor de n definido pelo usuário é positivo e,
#caso não seja, solicite outro valor até ser fornecido um valor positivo.

valor = int(input('Introduza um valor: '))

valor1 = 2
valor2 = 3
soma = 0

while valor < 0:
    int(input('Introduza um valor positivo: '))

while valor1 <= valor:
    print (valor1, valor2)
    valor1 = valor1 + 1
    valor2 = valor2 + 2
    soma =(soma) + (valor1/valor2)

print(soma)
