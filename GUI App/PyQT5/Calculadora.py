#Link do Video -> https://www.youtube.com/watch?v=8jrEVihl-E4

#NOTAS: layout é o corpo da janela

#Módulos
import PyQt5.QtWidgets as qtw

#Atributos da Janela
class MainWindow(qtw.QWidget):
    #Main Window
    def __init__(self):
        super().__init__()
        #Nome da Janela
        self.setWindowTitle('Calculadora')

        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()

    #Empty container
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        #Cor de fundo da janela
        container.setStyleSheet("background-color:#ff99ff")

        #Buttons
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter', clicked = self.func_result)
        btn_result.setStyleSheet("background-color: #009900")
        btn_clear = qtw.QPushButton('Clear', clicked = self.clear_calc)
        btn_clear.setStyleSheet("background-color: #cc0000")
        btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_mais = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        btn_menos = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        btn_x = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        btn_dividir = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))

        #Adicionar os buttons ao layout
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_result,5,2,1,2)
        container.layout().addWidget(btn_clear,5,0,1,2)
        container.layout().addWidget(btn_1,1,0)
        container.layout().addWidget(btn_2,1,1)
        container.layout().addWidget(btn_3,1,2)
        container.layout().addWidget(btn_4,2,0)
        container.layout().addWidget(btn_5,2,1)
        container.layout().addWidget(btn_6,2,2)
        container.layout().addWidget(btn_7,3,0)
        container.layout().addWidget(btn_8,3,1)
        container.layout().addWidget(btn_9,3,2)
        container.layout().addWidget(btn_0,4,1)
        container.layout().addWidget(btn_mais,3,3)
        container.layout().addWidget(btn_menos,4,3)
        container.layout().addWidget(btn_x,2,3)
        container.layout().addWidget(btn_dividir,1,3)

        #Mostrar os botões no layout
        self.layout().addWidget(container)

    def num_press(self,key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self,operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []

#Mostrar a janela
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()