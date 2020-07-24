#Criação de uma lista diferente

matriz=[[1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matriz)

matriz2 = [[lin[i] for lin in matriz] for i in range(4)]
print(matriz2)
