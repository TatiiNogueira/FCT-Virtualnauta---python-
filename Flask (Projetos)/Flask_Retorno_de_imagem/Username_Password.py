#NOTA: u -> username        p-> password

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TESLABETA17122020'
username = 'SATESLA'
password = 'SATESLA123'

#Verifica se o username e a password introduzidos são válidos
def Username_Password(u,p):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Emp_UserAT],[Emp_PasswordAT] from [dbo].[TBL_MUsers] where Emp_UserAT = '" + str(u) + "' and Emp_PasswordAT='" + str(p) + "'")
    #Se existirem dados com os mesmo que indicámos o programa irá retornar "True" caso contrário retorna "False"
    for row in cursor:
        return True
    return False

#Chamar a função
#print(Username_Password('508045932','2013508045932'))