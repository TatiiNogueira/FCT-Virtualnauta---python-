#Introzuzir a idade e aparece uma mensagem consoante a idade da pessoa

while True:
    x = int(input('Introduza a sua idade: '))

    if x < 18:
         print('Você é menor de idade.')
    elif x < 40:
        print('Você é adulto.')
    elif x < 60:
        print('Você é de meia idade.')
    else:
        print('Você é idoso.')
