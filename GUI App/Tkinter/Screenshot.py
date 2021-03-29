#Link do Video -> https://www.youtube.com/watch?v=Bzvm2_6gOvw

#Módulos
from tkinter import *
import time
import pyautogui

#Função tirar o ScreenShot
def print():
    #Tempo em que o ScreenShot foi tirado
    name  = int(round(time.time() * 1000))
    #Nome do ScreenShot
    name = 'Image' + '{}.png'.format(name)
    time.sleep(2)
    #A imagem é guardada na pasta do projeto aberta
    img = pyautogui.screenshot(name)
    #Mostrar a img
    img.show()
    #Faz com que a janela apreça novamente
    root.deiconify()

#Função fechar a janela após clicar no button ScreenShot
def delay():
    root.withdraw()
    #Mostra a img 30s depois
    root.after(30,print)

#Função Exit
def exit():
    root.destroy()

#Criar a janela
root = Tk()
#Cor de fundo da janela
root.configure(background='#ff9999')
#Titulo da janela
root.title('ScreenShot')
#Tamanho da janela
root.geometry('300x150')

#Buttons
#Button ScreenShot
Button(root, text='ScreenShot', font=('Arial',10,'bold'),height=1, width=14,background='#000000',fg='#ff9999',command=delay).place(x=95, y=20)
#Button Exit
Button(root, text='Exit', font=('Arial',10,'bold'),height=1, width=14,background='#000000',fg='#ff9999',command=exit).place(x=95, y=80)

#Mainloop - Inicializar a janela
root.mainloop()