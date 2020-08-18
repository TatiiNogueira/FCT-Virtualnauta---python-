#Visualizar a informação de ficheiros excel, realizar uma média de valores de colunas em expecifico
#Criar um gráfico de barras com as médias e criar um ficheiro excel com as médias

#Módulos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Ficheiro Excel 1 (Turno 1 e 2)
excel_file_1 = 'Pizaria12.xlsx'
#Ficheiro Excel 2 (Turno 3)
excel_file_2 = 'Pizaria3.xlsx'

#Ler os ficheiros Excel, sheet_name é o nome da folha excel
first_shift = pd.read_excel(excel_file_1, sheet_name='First')
second_shift = pd.read_excel(excel_file_1, sheet_name='Second')
#Como o ficheiro 2 só tem uma página não precisamos de colocal o nome da folha
third_shift = pd.read_excel(excel_file_2)

#Visualizar a informação de uma folha excel
print(first_shift)
#Visualizar uma coluna em expecifico de uma folha excel
print(second_shift['Product'])

#Combinação dos dados 
dados = pd.concat([first_shift, second_shift, third_shift])
#Imprimir os dados
print(dados)

#Verificar qual turno foi mais produtivo
#mean é a média
turnos = dados.groupby(['Shift']).mean()
#Indicação das colunas que queremos utilizar para verificar qual turno foi mais produtivo
#loc - Função que serve para selecionar várias linhas de dados em vez de um
productivity = turnos.loc[:,"Production Run Time (Min)":"Products Produced (Units)"]

#Irá imprimir a média de cada turno para as duas colunas
print(productivity)

#Realizar um gráfico de barras com os valores obtidos (Média das duas colunas)
productivity.plot(kind='bar')
plt.show()

#Guardar as médias calculadas num ficheiro excel
productivity.to_excel("Médias_Pizaria.xlsx")
