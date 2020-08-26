#Imprimir o código html de produtos de um site

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#Link
url = "http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH"

#Abrir o link
Client = uReq(url)

#Ler o html 
page_soup = soup(Client.read(), "html.parser")
#Fechar a página
Client.close()

#Encontar todos os produtos da página
containers = page_soup.findAll("div", {"class": "item-container"})

#Loop - Retirar informação (que será visualizada em código HTML) sobre cada produto
for container in containers:
    #Texto dentro da tag a 
    a = container.div.select("a")
    #Tags que contem as imagens e retirar o titulo
    title = container.select("div a img[title]")

    #Imprimir a informação
    print("Tag a: ", a, "\n")
    print("Nome do produto: ", title, "\n")
