#NOTA: "n" é o NIF, "a" é o Ano e "m" é o mês

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Vai buscar o nome do ficheiro DD cujo FC_Emp_NIF(n), FC_Ano(a) e FC_Mes(m) seja igual ao que indicamos
def getfileDD(n,a,m):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [FC_FicheiroDP] from [dbo].[TBL_FundosMOV] where FC_Emp_NIF ='" +  str(n) + "'AND FC_Ano ='" +  str(a) + "'AND FC_Mes ='" + str(m) + "'")
    for row in cursor:
        return row
    return False

#Chamar a função
#getfileDD('502793481','2017','4')
