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

#Clicar no tutorial Python Programming através do texto
driver.find_element_by_link_text("Python Programming").click()

#Tempo de espera
time.sleep(2)

#Clicar no tutorial dentro do tutorial Python Programming
driver.find_element_by_xpath('//*[@id="panel-146-0-0-0"]/figure/a/img').click()

#Tempo de espera
time.sleep(2)

#Clicar no botão Get Started através do id
driver.find_element_by_id("sow-button-19310003").click()

#Tempo de espera
time.sleep(3)

#Voltar atrás 3x
driver.back()
driver.back()
driver.back()

#Tempo de espera
time.sleep(3)

#Retomar para a página da frente
driver.forward()
time.sleep(3)
driver.forward()
