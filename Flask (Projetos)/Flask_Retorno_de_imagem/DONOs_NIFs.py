#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TESLABETA17122020'
username = 'SATESLA'
password = 'SATESLA123'

#Vai buscar o DONO_NIF correspondente ao NIF que nós indicamos
def Empresa_cliente(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [DONO_NIF] from [dbo].[TBL_MUsers] where Emp_NIF = '" + str(n) + "'")
    #Se existirem dados com os mesmo que indicámos o programa irá retornar "True" caso contrário retorna "False"
    for row in cursor:
        return True
    return False

#Vai buscar o DONO_NIF corresponde à empresa que fez o pedido
def Empresa_Chefe(u,p):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [DONO_NIF] from [dbo].[TBL_MUsers] where Emp_UserAT = '" + str(u) + "'and Emp_PasswordAT = '" + str(p) + "'")
    for row in cursor:
        return True
    return False

#Chamar a função
#Empresa_cliente('508896371')
#Empresa_Chefe('508896371','9XLWBGC9LHFX')