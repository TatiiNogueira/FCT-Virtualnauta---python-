#NOTA: "n" é o NIF, "a" é o Ano e "m" é o mês

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TESLABETA17122020'
username = 'SATESLA'
password = 'SATESLA123'

#Vai buscar o nome do ficheiro DMR cujo DMRAT_Emp_NIF(n), DMRAT_Ano(a) e DMRAT_Mes(m) seja igual ao que indicamos
def getfileDMR(n,a,m):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [DMRA_FicheiroDMR] from [dbo].[TBL_DMRAT] where DMRA_Emp_NIF ='" +  str(n) + "'AND DMRA_Ano ='" +  str(a) + "'AND DMRA_Mes ='" + str(m) + "'")
    for row in cursor:
        return row
    return False

#Chamar a função
#getfileDMR('502793481','2016','12')