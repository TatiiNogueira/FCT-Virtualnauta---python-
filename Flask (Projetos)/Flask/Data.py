#NOTA: n  é o ID que nós introduzimos

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TeslaV2230620'
username = 'SATESLA'
password = 'SATESLA123'

#Ver o valor correspondente ao ID n e à coluna Data
def Datas(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Data] from [dbo].[Flask] where ID = " + str(n) + "")
    for row in cursor:
        json_string = """{"Datas": {"Data": '""" + str(row[0]) + """'}}"""
        print(json_string)
    return json_string

#Chamar a função
#Datas()