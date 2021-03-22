#Link do Video -> https://www.youtube.com/watch?v=UnfmxnFpfdM

#Módulos
from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Username'), sg.Input(key='usuario')],
    [sg.Text('Password'),sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Login')]
]

#Janela
janela = sg.Window('Tela do Login',layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Login':
        #Se o username e a password forem iguais aos indicados, o programa imprime uma mensagem 
        if valores['usuario'] == 'user' and valores['senha'] == '12345':
            print("Bem vindo")