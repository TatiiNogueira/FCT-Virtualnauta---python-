#Mostra os ficheiros da nossa pasta (Nome, Data e Hora)

#Módulos
from subprocess import Popen, PIPE

pp = Popen(['ls', '-l'], stdout=PIPE, encoding='utf-8').communicate()[0]
print(pp)