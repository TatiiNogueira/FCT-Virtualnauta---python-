#NOTA: n  é o ID que nós introduzimos

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TeslaV2230620'
username = 'SATESLA'
password = 'SATESLA123'

#Elimina a linha correspondente ao ID n
def DELETE(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM [TeslaV2230620].[dbo].[Flask] WHERE ID = '" + str(n) + "'")
    cnxn.commit()
    return n

#Chamar a função
#DELETE('2')