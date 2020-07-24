# Módulos
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

# Aumentar janela
driver.maximize_window()

# Site
driver.get('https://web.whatsapp.com/')

# Tempo de espera
time.sleep(3)

# Confirmar que entramos no Whatshap
#print("Scan completo")

# Nome da pessoa ou grupo
people_1 = 'Mae'
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(people_1))

# Xpath comum em todas as pessoas + nome da pessoa
user.click()

# Tempo de espera
time.sleep(2)

# Campo de Escrita e mensagem
box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
box.send_keys('Adeus, não me mandes mensagem')

# Tempo de espera
time.sleep(2)

# Enviar a mensagem
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()