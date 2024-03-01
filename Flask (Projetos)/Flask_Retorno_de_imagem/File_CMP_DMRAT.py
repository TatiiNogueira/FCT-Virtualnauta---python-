#NOTA: "n" é o NIF, "a" é o Ano e "m" é o mês

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Vai buscar o nome do ficheiro DMR cujo DMRAT_Emp_NIF(n), DMRAT_Ano(a) e DMRAT_Mes(m) seja igual ao que indicamos
def getfileCMP_DMRAT(n,a,m):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [DMRA_FicheiroCMP] from [dbo].[TBL_DMRAT] where DMRA_Emp_NIF ='" +  str(n) + "'AND DMRA_Ano ='" +  str(a) + "'AND DMRA_Mes ='" + str(m) + "'")
    for row in cursor:
        return row
    return False

#Chamar a função
#getfileCMP_DMRAT('502793481','2016','12')
