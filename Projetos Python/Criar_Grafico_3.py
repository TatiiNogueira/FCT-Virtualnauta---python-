#Criação de um gráfico com barras
#NOTA: Para visualizar o gráfico tenho de clicar em Run Cell ou Run Below que fica por cima do "#%%"

#Run Cell ou Run Below
#%%

#Módulos
import matplotlib.pyplot as plt

#Número de meses
mes = [1, 2, 3]
#Quantidade de produtos vendidos
vendas = [100, 120, 80]
#Nome do mês
meses = ['Janeiro', 'Agosto', 'Dezembro']

#Criação do gráfico
#Indicação dos nomes dos meses
plt.xticks(mes, meses)
#Título
plt.title("Grafico")
#Texto para a zona do x
plt.xlabel("Meses")
#Texto para a zona do y
plt.ylabel("Quantidade vendida")
#Valores que quero colocar na tabela (x, y)
plt.bar(mes, vendas, align='center')
#Visualizar a tabela
plt.show
# %%