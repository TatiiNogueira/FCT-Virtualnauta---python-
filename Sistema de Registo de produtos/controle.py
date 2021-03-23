#Link dos Videos -> https://www.youtube.com/watch?v=SpHp0IfhorY
#                -> https://www.youtube.com/watch?v=Vb8EIdxl9HI

#Módulos
from PyQt5 import  uic,QtWidgets
import pyodbc

#Dados da Base de dados
server = 'LAPTOP-TN8OGODS'
database = 'Python_Testes/Estudo'
username = 'sa'
password = '1234'

#Função Principal - Vai ler os campos do formulário
def funcao_principal():
    #O lineEdit é o nome da textbox
    #formulario é o nosso formulário
    #text() é o que obtem o texto
    #TextBoxs
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    categoria=""

    #RadioButtons - Escolha da Categoria
    if formulario.radioButton.isChecked():
        print("Categoria Eletronicos selecionada")
        categoria = "Eletronicos"
    elif formulario.radioButton_2.isChecked():
        print("Categoria Informatica selecionada")
        categoria = "Informatica"
    elif formulario.radioButton_3.isChecked():
        print("Categoria Alimentos selecionada")
        categoria = "Alimentos"
    else:
        print("Nenhuma categoria foi selecionada")
        categoria=""

    #Imprimir o texto que foi colocado nas TextBoxs
    print("Código:",linha1)
    print("Descricao:",linha2)
    print("Preço:",linha3)

    #Guardar os dados na base de dados
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO [dbo].[Formulario_de_Produtos] ([Codigo],[Descricao],[Preco],[Categoria]) VALUES (?,?,?,?)",[linha1,linha2,linha3,categoria])
    cnxn.commit()
    cnxn.close()

app=QtWidgets.QApplication([])
#Nome do arquivo ui(É onde está o design da janela)
formulario=uic.loadUi("formulario.ui")
#Conecção com a função principal
#Quando clicarmos no botão Enviar o prorama irá executar a Função Principal
formulario.pushButton.clicked.connect(funcao_principal)

#Mostrar o formulario
formulario.show()
#Colocar o programa a correr/Chamar a função
app.exec()