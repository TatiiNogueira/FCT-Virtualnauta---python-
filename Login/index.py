#Fazer Login no Facebook, buscando as informação do login na base de dados SQL

#Módulos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyodbc
import time

#Função Ler  - Informação da base de dados 
def read(conn):
    cursor = conn.cursor()
    cursor.execute("select * from Facebook")
    for row in cursor:
        Email = row[0]
        Password = row[1]
        print("Email=", row[0], "\nPassword=", row[1])
    return (Email, Password)

#Ligação à base de dados
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-TN8OGODS;"
    "Database=Login;"
    "Trusted_Connection=yes;"
)

E, P = read(conn)
Email = E 
Password = P

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Link do site facebook
driver.get('https://www.facebook.com/?stype=lo&jlou=AffNdh7nRboHz0U_II5wU7gvUBRsreYHbTWmZPztAuk5pBqEBtkgm1eb_hOCZ6YzpZ2-jQR1PcFPdrPeBRFLevy3m4zikFGokv7OY5QUqLvhTQ&smuh=43850&lh=Ac-9XiodW_plPCPG')

#Tempo de espera
time.sleep(2)

#Inserir o Email
driver.find_element_by_xpath('//*[@id="email"]').send_keys(str(Email)) 

#Tempo de espera
time.sleep(1)

#Palavra Passe
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(str(Password))

#Tempo de espera
time.sleep(1)

#Clicar no botão Login
driver.find_element_by_id("u_0_b").click()

#Tempo de espera
time.sleep(3)

#Imprimir nome do utilizador
name = driver.find_element_by_xpath('//*[@id="navItem_100050977621600"]/a/div').text
print("Usename: ",name)

#Inserir nome na tabela
def create(conn):
    cursor = conn.cursor()
    cursor.execute(
        'insert into Username(Name) values(?);',(name))
    conn.commit()
    read(conn)
 
create(conn)
print("Username is ",name)

#Eliminar nome da tabela
#def delete(conn):
#    cursor = conn.cursor()
#    cursor.execute(
#       'delete from Username where Name = name'
#    )
#    conn.commit()
 
#delete(conn)

#Fechar janela
driver.close()
#Indicamos que fechamos a conecção
conn.close()
