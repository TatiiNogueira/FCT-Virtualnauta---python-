#Links -> https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/

'''NOTAS:
Para saber uma informação em especifico basta escrever
psutil.virtual_memory().informação
Em informção escrvermos o tipo de informação EX:total,percent,free...
'''

#Módulos
import psutil

#Percentagem da RAM usada
print('RAM memory used:', psutil.virtual_memory().percent)
#OU
print('RAM memory used:', psutil.virtual_memory()[2])

##############################################################

#Toda a informação sobre o armazenamento da RAM
print('Toda a informação:',psutil.virtual_memory())

##############################################################

#Obter as informação sobre o armazenado em Byte
def get_size(bytes, suffix='B'):
    factor = 1028
    for unit in [" "," K"," M"," G"," T"," P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

svmen = psutil.virtual_memory()
print(f"Total: {get_size(svmen.total)}")
print(f"Available: {get_size(svmen.total)}")
print(f"Used: {get_size(svmen.used)}")
