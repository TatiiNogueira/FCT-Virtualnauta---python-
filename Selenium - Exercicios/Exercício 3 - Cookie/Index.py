#Link do Video -> https://www.youtube.com/watch?v=OISEEL5eBqg

#Criação de um Boot para o jogo do Cookie (Cliques na bolacha de forma automática)

#Módulos
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#Passar o caminho do webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#Aumentar janela 
driver.maximize_window()

#Abrir um site 
driver.get("https://orteil.dashnet.org/cookieclicker/")

#Tempo de espera
driver.implicitly_wait(5)

#Encontrar o cookie
cookie = driver.find_element_by_id("bigCookie")

#Encontar a pontuação
cookie_count = driver.find_element_by_id("cookies")

#Encontar os elementos adicionais (O que posso comprar no jogo)
#Loop
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

#Cliques na cookie
actions = ActionChains(driver)
actions.click(cookie)

#Quantidade de loops e pontuação por segundo 
for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:    
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
