#NOTA: "n" é o NIF, "a" é o Ano e "m" é o mês
#O texto que queremos visualizar na interace/site tem de ser escrito em json

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TESLABETA17122020'
username = 'SATESLA'
password = 'SATESLA123'

#Ver todos o estado do documento DMRAT da empresa, onde os dados a baixo sejam iguais ao que nós indicarmos
#DMRAT_Emp_NIF -> n      DMRAT_Ano -> a      DMRAT_Mes -> m
def Status_DMRA(n,a,m):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [DMRA_Estado] from [dbo].[TBL_DMRAT] where DMRA_Emp_NIF ='" +  str(n) + "'AND DMRA_Ano ='" +  str(a) + "'AND DMRA_Mes ='" + str(m) + "'")
    #Texto inicial que queremos que apareça
    json_string = """{O Status do Emp_NIF """ + str(n) + """, Ano """ + str(a) + """, Mes """ + str(m) + """ é:["""
    #Os Emp_NIFs e o seu respetivo Emp_Empresa
    for row in cursor:
        json_string = json_string + row[0]
    #Fechamos o texto json
    json_string = json_string + """]}"""
    #print(json_string)
    return json_string

#Chamar a função
#Status_DMRA('502793481','2016','12')