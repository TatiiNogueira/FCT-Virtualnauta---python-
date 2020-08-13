#Imprimir o código da página, extrair informação da página e coloca dentro de um fciheiro excel

#Módulos
import requests,bs4,openpyxl,os

#Página
res = requests.get("https://www.custojusto.pt/porto/q/telemoveis")

#Saber que tipo de objeto é criado
print(type(res))

#Imprime o código da página
print(res.text)

#Validação se o dowload da página html foi bem sucedido
#Se existir algum erro até aqui o código irá parar
res.raise_for_status()

#Extrair informação da página 
#Irá pegar no texto e irá converter em uma extrutura html
objSoup=bs4.BeautifulSoup(res.text,features="html.parser")
#Mostrar o tipo do objSoup
print(type(objSoup))

#NOTA:Dentro do paranteses fica o nome da class (Se é titulo, preço...)
#Extrair o nome de todos os anúncios da página
#O b significa que está dentro da tag b
vetor_ad_name = objSoup.select('.title_related b')

#Extrair o preço de todos os anúncios da página
#O .container_related significa que quero todos os anúncios menos o que fica a passar vários anúncios diferentes
# O .prince_related significa o tempo
vetor_ad_price = objSoup.select('.container_related .price_related')

#Serve para confirmarmos que existe o mesmo número de títulos e preços
#Imprime o número de títulos
print(len(vetor_ad_name))
#Imprime o número de preços
print(len(vetor_ad_price))

#Salvar as informações no dicionário
#Vetor com anuncios
list_ad = []
#Indicamos que vamos pegar no número títulos e vamos subtrair 1
comp = len(vetor_ad_name)-1

#Ciclo for vai zer entre 0 e 39 
for i in range (0,comp):
    #Dicionário
    ad = {}
    #Tag do titulo
    ad["title"] = vetor_ad_name[i].getText(strip=True)
    #Tag do preço
    ad["price"] = vetor_ad_price[i].getText(strip=True)
    #Adiconar anúncio à lista de anúncios
    list_ad.append(ad)

#Local onde quero guardar o ficheiro exel
os.chdir('C:\\Users\\nogue\\Desktop\\Work\\Python')

#Criar o ficheiro exel
#Abrir e criar o ficheiro
workbook = openpyxl.Workbook()
#Criação da primeira folha do exel (sheet)
sheet = workbook['Sheet']
#Atribuição do nome da folha de exel
sheet.title = 'Anuncios'
#Definir o valor do row
row = 0

#O f vai ser o objeto da lista de anúncios
for f in list_ad:
    #Especificação do número da célula
    row = row + 1
    #Expecificação da coluna onde quero introduzir o titulo
    sheet.cell(row = row,column = 1).value = f['title']
    #Expecificação da coluna onde quero introduzir o preço
    sheet.cell(row=row, column = 2).value = f['price']

#Gravar o ficheiro
workbook.save('anuncios.xlsx')