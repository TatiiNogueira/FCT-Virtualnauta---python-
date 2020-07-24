#Módulos
from random import randint
from time import sleep

#Valore possíveis
computador = randint(0, 5)

#Texto
print ("Vou pensar num número entre 0 e 5")

#Jogador
player = int(input("Em que número pensei ?: "))

#Dar um pouco de suspense
print("Prossessando...")
sleep(3)

#Verificar se acertei o valor ou não
if player == computador:
    print("Parabéns! Ganhas te!")
else:
    print("Perdes te! Pensei no número {} e não no número {}".format(computador, player))