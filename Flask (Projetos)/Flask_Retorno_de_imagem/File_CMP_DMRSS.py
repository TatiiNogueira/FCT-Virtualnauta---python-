#NOTA: "n" é o NIF, "a" é o Ano e "m" é o mês

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TESLABETA17122020'
username = 'SATESLA'
password = 'SATESLA123'

#Vai buscar o nome do ficheiro CMP-DMRSS cujo DMRS_Emp_NIF(n), DMRS_Ano(a) e DMRS_Mes(m) seja igual ao que indicamos
def getfileCMP_DMRSS(n,a,m):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [DMRS_FicheiroCMP] from [dbo].[TBL_DMRSS] where DMRS_Emp_NIF ='" +  str(n) + "'AND DMRS_Ano ='" +  str(a) + "'AND DMRS_Mes ='" + str(m) + "'")
    for row in cursor:
        return row
    return False

#Chamar a função
#getfileCMP_DMRSS('502793481','2016','12')