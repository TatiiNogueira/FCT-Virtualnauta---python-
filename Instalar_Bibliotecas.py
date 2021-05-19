#Módulos
from pip._internal import main as pipmain

#Lista das bibliotecas
list = ('selenium','pyodbc')

for element in list:
    #Instalar as bibliotecas do python
    pipmain(['install', f"{element}"])
    #print(element)
print("INSTALAÇÃO CONLUÍDA, TODAS AS BIBLIOTECAS FORAM INSTALADAS")