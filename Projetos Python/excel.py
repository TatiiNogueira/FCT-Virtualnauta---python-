#Ler um ficheiro excel, e criar um "resumo"

#Módulos
import pandas as pd
import sweetviz as sv
import numpy as np 

#Ficheiro excel
x = pd.read_excel('C:\\Users\\nogue\\Desktop\\Work\\Python\\anuncios.xlsx')
#Imprimir a tabela/informação do excel
print(x) 

#Irá abrir uma janela com as informações da minha tabela por coluna
#Cria o reporte Exportar o reporte
sv.analyze(x).show_html()
