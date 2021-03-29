#Link do Video -> https://www.youtube.com/watch?v=x5LSTDdffFk

#NOTA: Posso usar o teclado do computador para executar as contas

#Módulos
import PySimpleGUI as sg 

#Tamanho tipo de letra e cor de fundo dos Buttons
#Números
bw: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#9999ff")}
#Sinais, %, CE e C
bt: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#6666ff")}
#Igual
bo: dict = {'size':(15,2), 'font':('Franklin Gothic Book', 24), 'button_color':("white","#0000e6"), 'focus':True}

layout: list = [
    #TextBox
    [sg.Text('0', size=(18,1), justification='right', background_color='#0000e6', text_color='white',font=('Digital-7',48), relief='sunken', key="_DISPLAY_")],
    #Buttons introdução do Texto
    [sg.Button('C',**bt), sg.Button('CE',**bt), sg.Button('%',**bt), sg.Button("/",**bt)],
    [sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button("*",**bt)],
    [sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button("-",**bt)],
    [sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button("+",**bt)],    
    [sg.Button('0',**bw), sg.Button('.',**bw), sg.Button('=',**bo, bind_return_key=True)]]

#Janela
window: object = sg.Window('Calculadora', layout=layout, background_color="#ccccff", size=(580, 660), return_keyboard_events=True)

#Calculator Functions
var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

#Helper Functions - Cria uma sequência consolidada de números das listas da frente e de trás
def format_number() -> float:
    return float(''.join(var['front']) + '.' + ''.join(var['back']))

#Atualiza o display da calculadora depois de um evento click
def update_display(display_value: str):
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

#Função de click
def number_click(event: str):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())
    
#Função Clear
def clear_click():
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False 

#Função para os sinais
def operator_click(event: str):
    ''' + - / * button click event '''
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()

#Função do Buuton =
def calculate_click():
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()    
    except:
        update_display("ERROR! DIV/0")
        clear_click()

#Main Event Loop
while True:
    event, values = window.read()
    if event is None:
        break
    #Se precionar um botão
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    #Se clicar no botão C ou CE da calculadora ou ESC do teclado irá limpar os dados
    #Escape:27 é o botão "Esc"
    if event in ['Escape:27','C','CE']:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    #Se clicar num dos sinais
    if event in ['+','-','*','/']:
        operator_click(event)
    #Se clicar no =
    if event == '=':
        calculate_click()
    #Se clicar no ponto
    if event == '.':
        var['decimal'] = True
    #Se clicar no %
    if event == '%':
        update_display(var['result'] / 100.0)