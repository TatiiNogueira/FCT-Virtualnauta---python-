#Link do Video -> https://www.youtube.com/watch?v=O4NrNzKZfoQ

#Módulos
import calendar
from tkinter import *

#Criar a janela
root = Tk()
#Cor de fundo da janela
root.configure(background='black')
#Titulo da janela
root.title('Calendário')

#Indicação do ano do calendário
cal = calendar.calendar(2021)

#Labels
#Titulo
Label(root, text='My Calendar', font=('times',30,'bold'),background='#000000',foreground='white').grid(row=1,column=1)
#Calendário
Label(root,text=cal, font=('Consolas 10 bold'),background='#00cc66',foreground='white').grid(row=2,column=1,padx=20)

#Mainloop - Inicializar a janela
root.mainloop()