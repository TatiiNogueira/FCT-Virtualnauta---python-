#Criação de um gráfico com 3y
#NOTA: Para visualizar o gráfico tenho de clicar em Run Cell ou Run Below que fica por cima do "#%%"

#Run Cell ou Run Below
#%%

#Módulos
import matplotlib.pyplot as plt

#Número de meses
mes = [1, 2, 3, 4, 5, 6]
#Quantidade de produtos vendidos
loja_1 = [100, 120, 80, 300, 200, 50]
loja_2 = [250, 90, 60, 150, 300, 290]
loja_3 = [40, 30, 60, 190, 250, 20]

#Criação do gráfico
#Valores do x e dos y e indicação de que a que cor corresponde cada loja
plt.stackplot(mes, loja_1, loja_2, loja_3, labels=['Loja 1', 'Loja 2', 'Loja 3'])
#Título
plt.title("Grafico")
#Texto para a zona do x
plt.xlabel("Mes")
#Texto para a zona do y
plt.ylabel("Quantidade vendida")
#Indicação que queremos colocar a legenda (Nome das lojas e a sua respetiva cor)
plt.legend(loc='upper left')
#Visualizar a tabela
plt.show
# %%