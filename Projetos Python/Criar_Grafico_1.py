#Criação de um gráfico
#NOTA: Para visualizar o gráfico tenho de clicar em Run Cell ou Run Below que fica por cima do "#%%"

#Run Cell ou Run Below
#%%

#Módulos
import matplotlib.pyplot as plt

#Número de meses
mes = [1, 2, 3, 4, 5, 6]
#Quantidade de produtos vendidos
vendas = [100, 120, 80, 300, 200, 50]

#Criação do gráfico
#Título
plt.title("Grafico")
#Texto para a zona do x
plt.xlabel("Mes")
#Texto para a zona do y
plt.ylabel("Quantidade vendida")
#Valores que quero colocar na tabela (x, y)
plt.plot(mes, vendas)
#Visualizar a tabela
plt.show
# %%