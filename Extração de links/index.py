#Extração dos ultimos 10 links de um site

#Módulos
from selenium import webdriver
import time

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Site
driver.get('https://www.occ.pt/pt/noticias/') 

#Tempo de espera
time.sleep(2)

#Elementos 
noticia_1 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[2]/td/a')
noticia_2 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[4]/td/a')
noticia_3 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[7]/td/a')
noticia_4 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[10]/td/a')
noticia_5 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[13]/td/a')
noticia_6 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[15]/td/a')
noticia_7 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[18]/td/a')
noticia_8 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[21]/td/a')
noticia_9 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[24]/td/a')
noticia_10 = driver.find_element_by_xpath('//*[@id="frm_detalhe"]/table[3]/tbody/tr[26]/td/a')

#Tempo de espera
time.sleep(2)

#Imprimir os Links
print ("Noticia 1: " + noticia_1.get_attribute("href"))
print ("Noticia 2: " + noticia_2.get_attribute("href"))
print ("Noticia 3: " + noticia_3.get_attribute("href"))
print ("Noticia 4: " + noticia_4.get_attribute("href"))
print ("Noticia 5: " + noticia_5.get_attribute("href"))
print ("Noticia 6: " + noticia_6.get_attribute("href"))
print ("Noticia 7: " + noticia_7.get_attribute("href"))
print ("Noticia 8: " + noticia_8.get_attribute("href"))
print ("Noticia 9: " + noticia_9.get_attribute("href"))
print ("Noticia 10: " + noticia_10.get_attribute("href"))

#Tempo de espera
time.sleep(2)

#Fechar a janela
driver.close()
