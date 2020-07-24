#Módulos
from selenium import webdriver
import time

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Para ver se está a funcionar, utilizo um site qualquer
driver.get('https://eco.sapo.pt/ultimas/') 

#Tempo de espera
time.sleep(5)

#Clicar no botão de Aceitar
button_input = '//*[@id="qcCmpButtons"]/button[2]'
driver.find_element_by_xpath(button_input).click()

#Encontrar Elemento
link_input = '//*[@id="main"]/div[1]/div/div/div/article[1]'
driver.find_element_by_xpath(link_input).click()
time.sleep(5)