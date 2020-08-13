#Imprimir texto da última notícia do site através do "class name" (Classe)

#Módulos
from selenium import webdriver
import time

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Site
driver.get('https://eco.sapo.pt/ultimas') 

#Tempo de espera
time.sleep(2)

#Clicar no aceitar
driver.find_element_by_xpath('//*[@id="qcCmpButtons"]/button[2]').click()

#Abrir a notícia
driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/article[1]/a').click()

#Tempo de espera
time.sleep(2)

#Xpath
titulo = driver.find_element_by_class_name('title').text
sub_titulo = driver.find_element_by_class_name('entry__lead').text
texto = driver.find_element_by_class_name('entry__content').text
hora = driver.find_element_by_class_name('meta__time').text

#Tempo de espera
time.sleep(2)

#Imprimmir a informção da notícia
print("Título: " + titulo)
print("Sub título: " + sub_titulo)
print("Texto: " + texto)
print("Hora: " + hora)

#Fechar a janela
driver.close()