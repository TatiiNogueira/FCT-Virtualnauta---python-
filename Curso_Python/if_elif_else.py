idade = int(input("Indica a tua idade: "))

if idade == 1:
    print("És um bebé")
elif idade > 1 and idade < 12:
    print("És uma criança")
elif idade >= 12 and idade < 18:
    print("És um adulescente")
elif idade >= 18 and idade < 40:
    print("És um adulto")
elif idade >= 40 and idade < 60:
    print("Estás na meia idade")
else:
    print("És velho")