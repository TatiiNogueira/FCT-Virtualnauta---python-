#Alterar o ID e o select CSS

#Módulos
from selenium.webdriver.common.by import By

#Criação de classes que representam objetos que queremos encontar
#Esta classe define todos os localizadores da Página Principal(page.py)
#Queremos que clique no botão Go através do seu ID
class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass