#Módulos
from selenium import webdriver
import time

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Site
driver.get('https://eco.sapo.pt/ultimas/') 

#Tempo de espera
time.sleep(2)

#Clicar no aceitar
button_acept = '//*[@id="qcCmpButtons"]/button[2]'
driver.find_element_by_xpath(button_acept).click()

#Abrir a notícia
driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/article[1]/a').click()

#Tempo de espera
time.sleep(2)

#Xpath 
titulo = driver.find_element_by_xpath('//*[@id="post-649732"]/div/div[1]/header/h1').text
sub_titulo = driver.find_element_by_xpath('//*[@id="post-649732"]/div/div[1]/header/h2').text
texto = driver.find_element_by_xpath('//*[@id="post-649732"]/div/div[1]/div[1]').text
hora = driver.find_element_by_xpath('//*[@id="post-649732"]/div/div[1]/header/div[2]/div/div[1]/ul/li[2]').text

#Tempo de espera
time.sleep(2)

#Imprimmir a informção da notícia
print("Título: " + titulo)
print("Sub título: " + sub_titulo)
print("Texto: " + texto)
print("Hora: " + hora)

#Tempo de espera
time.sleep(2)

#Fechar a janela
driver.close()