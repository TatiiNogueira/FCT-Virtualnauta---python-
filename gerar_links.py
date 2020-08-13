#Geral um link ou vários

#GERAL UM LINK
#Ano que desejo
year = '2019'
#Link comum para todos os anos
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

#Combinação do link (str) + ano (year)
url = str.format(year)

#Imprimir o link
print(url)

#GERAL VÁRIOS LINKS
#Anos que desejo
years = [2015,2016,2017,2018]
#Link comum para todos os anos
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

#Cliclo for , para a criação dos links
for year in years:
  url = str.format(year)
  print(url)