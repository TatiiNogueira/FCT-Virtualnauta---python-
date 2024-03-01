#NOTA: n  é o ID que nós introduzimos

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Ver o valor correspondente ao ID n e à coluna Titulo
def Titulos(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Titulo] from [dbo].[Flask] where ID = " + str(n) + "")
    for row in cursor:
        json_string = """{"Titulos": {"Titulo": '""" + row[0] + """'}}"""
    return json_string

#Chamar a função
#Titulos()
