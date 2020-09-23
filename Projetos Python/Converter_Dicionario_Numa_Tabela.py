#Converter um dicionário numa tabela

#Módulos
import pandas as pd

#Dicionário
Dic = {'Day':[1,2,3,4,5], "Visitors":[100,450,500,945,130], 'Taxa_Regecao':[20,64,67,84,451]}

#Conversão do dicionário
df = pd.DataFrame(Dic)

#Visualizar a tabela
print(df)