#Retirar informação de um site

#Módulos
from bs4 import BeautifulSoup
import requests
import csv

url = requests.get('http://coreyms.com').text

#Analiza o HTML da página
soup = BeautifulSoup(url, 'lxml')

#Abri um fiheiro CSV e permitir que escreva dentro do mesmo
csv_file = open('Web Scraping 3.1.csv', 'w')
csv_writer = csv.writer(csv_file)
#Texto que queremos introduzir no ficheiro CSV
csv_writer.writerow(['Titulo', 'Texto', 'video_link'])

#Criamos um loop que irá retornar uma lista com as informações que desejamos de todos os artigos
for article in soup.find_all('article'):
    title = article.h2.a.text
    text = article.find('div', class_='entry-content').p.text

    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        video_id = video_src.split('/')[4]
        video_id = video_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        yt_link = None
    print(yt_link)

    print()

    #Dados que serão introduzidos no ficheiro CSV
    csv_writer.writerow([title, text, yt_link])

#Fechar o fecheiro CSV
csv_file.close()
