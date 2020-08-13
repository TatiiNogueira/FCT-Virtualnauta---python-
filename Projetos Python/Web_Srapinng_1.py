#Imprimir a tabela da página, utilizando a biblioteca pandas

#Módulos
import pandas as pd

#Link
url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'

#Indicação de queremos "ler" o html que está na página que indicamos
#E indicamos que queremos ler a tabela apartir do primeiro elemento
#Lembrando que a contagem começa sempre pelo 0
df = pd.read_html(url, header = 0)
#Imprimimos a tabela
print(df)

#Saber quantas tabelas existem na página
print(len(df))

#Selecionar uma tabela em expecifico(Neste caso a primeira)
print(df[0])
