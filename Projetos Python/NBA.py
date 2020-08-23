#Imprimir a tabela da página, utilizando a biblioteca pandas
#Colocar a tabela dentro de um ficheiro Excel
#Depois passar o ficheiro Excel para a base de dados

#Módulos
import pandas as pd

#Link
url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'

#Indicação de queremos "ler" o html que está na página que indicamos
#E indicamos que queremos ler a tabela apartir do primeiro elemento
#Lembrando que a contagem começa sempre pelo 0
table = pd.read_html(url, header = 0)
#Imprimimos a tabela
print(table)

#Combinar os dados
dados = pd.concat(table)

#Guardar a tabela num ficheiro Excel
dados.to_excel('NBA.xlsx')