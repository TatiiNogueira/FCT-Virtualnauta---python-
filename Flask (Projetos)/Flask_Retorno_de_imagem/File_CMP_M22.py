#NOTA: "n" é o NIF, "a" é o Ano e "m" é o mês

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Vai buscar o nome do ficheiro DP cujo M22_Emp_NIF(n) e M22_Ano(a) seja igual ao que indicamos
def getfileCMP_M22(n,a):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [M22_FicheiroCMP] from [dbo].[TBL_M22MOV] where M22_Emp_NIF ='" +  str(n) + "'AND M22_Ano ='" +  str(a) + "'")
    for row in cursor:
        return row
    return False

#Chamar a função
#getfileCMP_M22('502793481','2019')
