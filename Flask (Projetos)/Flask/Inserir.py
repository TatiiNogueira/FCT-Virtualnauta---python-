#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TeslaV2230620'
username = 'SATESLA'
password = 'SATESLA123'

#Introduzir os valores na base de dados
def INSERE(a,b,c,d,e,f,g):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("INSERT into [dbo].[Flask] ([Titulo],[Grador],[Categoria],[Descricao],[Data],[Sala],[ImagemID]) VALUES(?,?,?,?,?,?,?)", [a,b,c,d,e,f,g])
    cnxn.commit()
    json_string = """{"Todos":{"Titulo": '""" + a + """'; "Grador": '""" + b + """'; "Categoria": '""" + c + """'; "Descricao": '""" + d + """'; "Data": '""" + e + """'; "Sala": '""" + f + """'; "ImagemID": '""" + g + """'}"""
    print(json_string)
    return a,b,c,d,e,f,g
