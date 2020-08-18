#Criação de uma espécie de tabela, que é vista no terminal

#Módulos
import pandas as pd
import numpy as np

#Criação de uma lista
A = pd.Series([5,4,3,2,1])
#Visualização da lista A - Aparecerá o número da posição 0, 1 ,2 ....
print(A)

#Apenas para fazer uma separação entre as tabelas
print("............................................")

#Criação de duas listas onde a posição dos números irá aparecer em letras ao invés de números
A = pd.Series([5,4,3,2,1], index=['a','b','c','d','e'])
print(A)
B = pd.Series([9,8,7,6,5], index=['a','b','c','d','e'])
print("............................................")

#Junção das duas listas para formar uma espécie de tabela e o nome das colunas
dictA = {'Lista A':A, 'Lista B':B}
df = pd.DataFrame(dictA)
print(df)
