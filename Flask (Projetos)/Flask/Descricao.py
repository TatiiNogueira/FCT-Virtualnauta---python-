#NOTA: n  é o ID que nós introduzimos

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Ver o valor correspondente ao ID n e à coluna Descricao
def Descricoes(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Descricao] from [dbo].[Flask] where ID = " + str(n) + "")
    for row in cursor:
        json_string = """{"Descricoes": {"Descricao": '""" + row[0] + """'}}"""
        print(json_string)
    return json_string

#Chamar a função
#Descricoes()
