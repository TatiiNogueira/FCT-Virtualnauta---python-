#NOTA: n  é o ID que nós introduzimos

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Ver o valore correspondente ao ID n e às colunas Valor_1 e Valor_2
def Buscar_Menos(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Valor_1],[Valor_2] from [dbo].[Flask_Contas] where ID = " + str(n) + "")
    #Executa a conta
    for row in cursor:
        B = row[0] - row[1]

        #Guarda a conta na tabela
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        cursor.execute("UPDATE [dbo].[Flask_Contas] set [Resultado_Menos] = ?", [B])
        cnxn.commit()
        json_string = """{"Conta": """ + str(row[0]) + """ - """ + str(row[1]) + """ {"Resultado": '""" + str(B) + """'}}"""
        print(json_string)
    return json_string

#Chamar a função
#Buscar_Menos("5.00","8.00","-3")
