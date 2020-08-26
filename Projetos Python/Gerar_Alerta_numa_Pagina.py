#Gerar um alerta numa página

#Módulos
from selenium import webdriver 
  
#Caminho Webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
  
#Site
driver.get("https://www.geeksforgeeks.org/") 
   
#Gerar o alerta e o texto que quero que a apareça
driver.execute_script("alert('Alert via selenium')") 