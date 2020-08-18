#Imprimir a informação do site da worten
#Através do link que a pessoa irá inserir  - Para inserir o link a pessoa tem de selecioner as caracteristicas que deseja (Selecionando as CheckBoxs)
#Copia o link e cola no programa

#Módulos
from selenium import webdriver
import time

#Introdução do links
print("Vá ao site da worten escolha o produto que deseja ver, selecione as caracteristicas que deseja (Selecionando as CheckBoxs), copie o link e introduza a baixo")
x = input('Introduza o link: ')

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Link do site que a pessoa introduzir
driver.get(x)

#Tempo de espera
time.sleep(2)

#Imprimir informação
#Imprime tudo da lista
elementos = driver.find_element_by_xpath('//*[@id="products-list-block"]').text
print(elementos)

#Fechar janela
driver.close()
