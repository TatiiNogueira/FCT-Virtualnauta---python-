#Com esta página podemos abstrair todas as ações comuns em um local central e aproveitá-las 
#em qualquer Objeto de Página que considerarmos adequado.

#Métodos
from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver 
    
class MainPage(BasePage):
    search_text_element = SearchTextElement()
    
#Método - Vai dizer se o título da página corresponnde ao que nós desejamos
#Diz se a String Python está no título
    def is_title_matches(self):
        return "Python" in self.driver.title    
 
#Encontrar o elemento que é indicado pelo localizador que colocar mos 
#à frente de sel.driver.find_element
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

#Se a String "No result found." não for encontrado significa que tudo correu bem
class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
