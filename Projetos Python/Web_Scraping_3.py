#Retirar informação de um site

#Módulos
from bs4 import BeautifulSoup
import requests

url = requests.get('http://coreyms.com').text

#Analiza o HTML da página
soup = BeautifulSoup(url, 'lxml')

#Este print permite me visualizar o código html da página
#print(soup.prettify())

#Encontrar o primeiro artigo
article =  soup.find('article')
#Imprime o HTML todo junto
print(article)
print("--------------------------------------------------------------------------------------------------------------------------------")
print("................................................................................................................................")
print("--------------------------------------------------------------------------------------------------------------------------------")
#Imprime o HTML todo organizado
print(article.prettify())
print("--------------------------------------------------------------------------------------------------------------------------------")
print("................................................................................................................................")
print("--------------------------------------------------------------------------------------------------------------------------------")
#Imprime o texto do HTML
print(article.text)
print("--------------------------------------------------------------------------------------------------------------------------------")
print("................................................................................................................................")
print("--------------------------------------------------------------------------------------------------------------------------------")

#Procurar o título do artigo (O h2 é a tag onde o título se encontra)
title = article.h2.a.text
print(title)
print("--------------------------------------")

#Procurar o texto (O p significa 1º parágrafo)
text = article.find('div', class_='entry-content').p.text
print(text)
print("--------------------------------------")

#Procurar o link do video
video_src = article.find('iframe', class_='youtube-player')['src']
print(video_src)
print("--------------------------------------")

#Mostrar o link dividido em partes, separando na zona em que tem uma barra
id = video_src.split('/')
print(id)
print("--------------------------------------")

#Mostra apenas o quarto "elemento" que foi dividido através de uma barra
video_id = video_src.split('/')[4]
#Mostra apenas o primeiro "elemento" que foi dividido através do ?
video_id = video_id.split('?')[0]
print(video_id)
print("--------------------------------------")

#Link comum para todos os videos do youtube e indicamos que queremos utilizar o id
#Esse id vem do video_id
yt_link = f'https://youtube.com/watch?v={video_id}'
print(yt_link)
