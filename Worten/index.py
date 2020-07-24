#Módulos
from selenium import webdriver
import pyodbc
import time

#Ligação à base de dados
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-TN8OGODS;"
    "Database=End;"
    "Trusted_Connection=yes;"
)

#Introdução do links
print("Vá ao site da worten escolha o produto que deseja ver, selecione as caracteristicas que deseja (Selecionando as CheckBoxs), copie o link e introduza a baixo")
x = input('Introduza o link: ')

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Link do site que a pessoa introduzir
driver.get(x)

#Tempo de espera
time.sleep(2)

#Imprimir informação
#Imprime tudo da lista
elementos = driver.find_element_by_xpath('//*[@id="products-list-block"]').text
print(elementos)

#Inserir informações na tabela
#def create(conn):
#    cursor = conn.cursor()
 #   cursor.execute(
  #      'insert into Final(Nome) values(?);', (elementos))
   # conn.commit()

#create(conn)

#Fechar janela
driver.close()
#Indicamos que fechamos a conecção
conn.close()