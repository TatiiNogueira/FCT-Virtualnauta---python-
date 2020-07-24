#Crie um algoritmo que leia um valor e a partir disso faça:
#(1) se for um valor negativo,
#mostre o módulo (valor sem sinal) do valor (Alterar o sinal de + para -);
#(2) se for um valor maior do que 10, solicite outro valor
#e mostre a diferença entre eles;
#(3) Caso o valor não seja de nenhuma condição anterior,
#mostre o valor dividido por 5.

Valor = int(input('Introduza um valor: '))
    
if Valor < 0:
    Inversão = Valor * -1
    print(Inversão)

elif Valor > 10:
    Valor2 = int(input('Introduza outro valor: '))
    Diferença = Valor - Valor2
    print(Diferença)

else:
    Divisão = Valor/5
    print(Divisão)



    

    
