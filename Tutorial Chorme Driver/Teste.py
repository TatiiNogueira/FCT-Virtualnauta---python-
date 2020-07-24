from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Para ver se está a funcionar, utilizo um site qualquer
driver.get('https://eco.sapo.pt')

