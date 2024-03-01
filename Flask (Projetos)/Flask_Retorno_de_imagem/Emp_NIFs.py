#NOTA: n  é o Dono_NIF que nós introduzimos
#O texto que queremos visualizar na interace/site tem de ser escrito em json

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Ver todos os Emp_NIFs cujo DONO_NIF é o que foi indicado ou seja o n
def EmpsNIFs(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Emp_NIF] from [dbo].[TBL_MUsers] where Dono_NIF = " + str(n) + "")
    #Texto inicial que queremos que apareça
    json_string = """{""" + str(n) + """":["""
    #Os Emp_NIFs
    for row in cursor:
        json_string = json_string + row[0] + """;"""
    #Fechamos o texto json
    json_string = json_string + """]}"""
    #print(json_string)
    return json_string

#Chamar a função
#EmpsNIFs('502793481')
