#Abrimos a janela do google (neste caso mas pode ser outra janela qualquer)
#inserimos o texto e fazemos enter para pesquisar

#Módulos
import pyautogui

#Saber as coordenadas da barra de pesquisa
print(pyautogui.position())
#Fazer click sobre a barra de pesquisa e indicamos as coordenadas do x e do y
pyautogui.click(1264, 41)
#Indicamos o texto que queremos escrever
pyautogui.typewrite("Hello World")
#Fazer enter
pyautogui.typewrite(["enter"])
