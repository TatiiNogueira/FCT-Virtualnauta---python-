#Exemplo 1
print("Qual é o seu nome?")
nome = input()
print("Welcome",nome)

#Exemplo 2
name = input("Qual é o seu nome? ")
print("Welcome %s" %name)

#Exemplo 3
n = input("Qual é o seu nome? ")
i = input("Qual é a sua idade? ")
print("%s tem %s anos" %(n, i))

#Exemplo 4
animal = input("Qual é o nome do seu animal de estimação? ")
print('O nome do seu animal de estimação é {}'.format(animal))

#Exemplo 5
gelado = input("Qual é o seu sabor de gelado favorito? ")
print(f'O seu sabor de gelado favorito é {gelado}')

#Exemplo 6
ano = input("Vamos descobrir em que ano nasceste, diz me a tua idade atual: ")
print(f"Nasceste em {2021-int(ano)}")

#Exemplo 7
fruta = int(input("Quantas frutas comes por dia? "))
print(f"Por dia tu comes {fruta}")