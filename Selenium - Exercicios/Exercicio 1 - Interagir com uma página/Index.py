#Módulos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Abrir um site 
driver.get("https://techwithtim.net/")

#Obter o título do site
print(driver.title)

#Encontar a barra de pesquisa do site
search = driver.find_element_by_name("s")

#Indicação o que queremos procurar
search.send_keys("test")

#Retornar resultado da pesquisa
search.send_keys(Keys.RETURN)

#Tempo de espera
time.sleep(5)

#Imprimir o texto dos "cartões"
main = driver.find_element_by_id("main")
print(main.text)

#Fechar o browser
driver.quit()
