#NOTA: "n" é o NIF, "a" é o Ano e "m" é o mês
#O texto que queremos visualizar na interace/site tem de ser escrito em json

#Módulos
import pyodbc

#Dados da Base de dados
server = '195.23.10.76\LAB1'
database = 'TESLABETA17122020'
username = 'SATESLA'
password = 'SATESLA123'

#Ver todos o estado do documento saft da empresa, onde os dados a baixo sejam iguais ao que nós indicarmos
#SAFT_NIF -> n      Saft_Ano -> a      SAFT_Mes -> m
def Status_Saft(n,a,m):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [SAFT_Status] from [dbo].[TBL_SAFTMOV] where SAFT_NIF ='" +  str(n) + "'AND SAFT_Ano ='" +  str(a) + "'AND SAFT_Mes ='" + str(m) + "'")
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
#Status('508045932','2020','11')