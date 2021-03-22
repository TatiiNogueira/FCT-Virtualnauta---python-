#NOTA: n  é o ID que nós introduzimos

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TeslaV2230620'
username = 'SATESLA'
password = 'SATESLA123'

#Ver todos os valores correspondentes ao ID n
def TodosValores():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Titulo],[Grador],[Categoria],[Descricao],[Data],[Sala],[ImagemID] from [dbo].[Flask]")
    json_string = """{"TodosValores":["""
    for row in cursor:
        json_string = json_string + """{"Titulo": '""" + row[0] + """'; "Grador": '""" + row[1] + """'; "Categoria": '""" + row[2] + """'; "Descricao": '""" + row[3] + """'; "Data": '""" + str(row[4]) + """'; "Sala": '""" + row[5] + """'; "ImagemID": '""" + str(row[6]) + """'}"""
    json_string = json_string + """]}"""
    print(json_string)
    return json_string

#Chamar a função
TodosValores()