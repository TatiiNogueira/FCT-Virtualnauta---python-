#Instalação das bibliotecas do python de forma automática

#Módulos
from pip._internal import main as pipmain

#Lista das bibliotecas
list = ('pika','beautifulsoup4','bs4','flask','matplotlib','numpy','openpyxl','pyPDF2','selenium','pandas','django','gunicorn')

for element in list:
    #Instalar as bibliotecas do python
    pipmain(['install', f"{element}"])
    #print(element)
print("INSTALAÇÃO CONLUÍDA, TODAS AS BIBLIOTECAS FORAM INSTALADAS")