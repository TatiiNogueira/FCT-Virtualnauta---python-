#NOTA: n  é o ID que nós introduzimos

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TeslaV2230620'
username = 'SATESLA'
password = 'SATESLA123'

#Ver o valor correspondente ao ID n e à coluna Sala
def Salas(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Sala] from [dbo].[Flask] where ID = " + str(n) + "")
    for row in cursor:
        json_string = """{"Salas": {"Sala": '""" + row[0] + """'}}"""
    return json_string
