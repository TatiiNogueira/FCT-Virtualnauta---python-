#NOTA: n  é o Dono_NIF que nós introduzimos
#O texto que queremos visualizar na interace/site tem de ser escrito em json
#Se existem valores na base de dados que seijam "NULL" ou "NoneType",
#o programa coloca um "-" no lugar onde deveriam ficar os valores

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TESLABETA17122020'
username = 'SATESLA'
password = 'SATESLA123'

#Ver todos os Emp_NIFs, o seu respetivo Emp_Empresa e os emails cujo DONO_NIF é o que foi indicado ou seja o n
def Informacoes(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Emp_NIF],[Emp_Empresa],[Emp_Email],[Emp_EmailG] from [dbo].[TBL_MUsers] where Dono_NIF = " + str(n) + "")
    #Texto inicial que queremos que apareça
    json_string = """{"Informações das empresas cujo Dono_NIF é """ + str(n) + """":["""
    #Os Emp_NIFs, o seu respetivo Emp_Empresa e os seus emails
    for row in cursor:
        if row[2] == 'NULL' or 'NoneType':
            row[2] = '-'
        else:
            pass
        if row[3] == 'NULL' or 'NoneType':
            row[3] = '-'
        else:
            pass
        json_string = json_string + """{"Emp_NIF": '""" + row[0] + """'; "Emp_Empresa": '""" + row[1] + """'; "Emp_Email": '""" + row[2] + """'; "Emp_EmailG": '""" + row[3] + """'}"""
    #Fechamos o texto json
    json_string = json_string + """]}"""
    #print(json_string)
    return json_string

#Chamar a função
#Informacoes('502793481')