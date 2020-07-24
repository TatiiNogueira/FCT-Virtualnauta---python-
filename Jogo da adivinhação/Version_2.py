#Módulos
from random import randint
from time import sleep

#Valore possíveis
computador = randint(0, 10)

#Texto
print ("Vou pensar num número entre 0 e 10")

acertou = False
#Número de palpites
palpites = 0

#Enquanto o jogador não acertar, irá aparecer para o jogador tentar novamente
while not acertou:
    player = int(input("Em que número pensei ? "))
    #Por cada tentativa acrescento mais um palpite
    palpites += 1

    #Se o valor for igual ao do pc ele irá imprimir a mensagem acertou
    if player == computador:
        acertou = True
    #Se errar o valor ele irá me dar dicas
    else:
        if player < computador:
            print("É um número maior que esse, tente outravés")
        elif player > computador:
            print("É um número mais pequeno que esse, tente outravés")

#Mensagem
print("Acertou com {} tentativas".format(palpites))