#NOTA: n  é o Dono_NIF que nós introduzimos
#O texto que queremos visualizar na interace/site tem de ser escrito em json
#Se existem valores na base de dados que seijam "NULL" ou "NoneType",
#o programa coloca um "-" no lugar onde deveriam ficar os valores

#Módulos
import pyodbc

#Dados da Base de dados
server = ''
database = ''
username = ''
password = ''

#Ver todos os Emp_NIFs e o seu respetivo Emp_Empresa cujo DONO_NIF é o que foi indicado ou seja o n
def Autenticacoes(n):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("select [Emp_NIF],[Emp_Empresa],[Emp_UserAT],[Emp_PasswordAT],[Emp_UserSS],[Emp_PasswordSS],[Emp_IAPMEIUser],[Emp_IAPMEIPass],[Emp_RelUnicoUser],[Emp_RelUnicoPass],[Emp_INEUser],[Emp_INEPass],[Emp_IEFPUser],[Emp_IEFPPass],[Emp_IEFPOnlineUser],[Emp_IEFPOnlinePass],[Emp_SILIAMBUser],[Emp_SILIAMBPass],[Emp_SIRAPAUser],[Emp_SIRAPAPass],[Emp_B2020User],[Emp_B2020Pass],[Emp_SoftFaturacaoUser],[Emp_SoftFaturacaoPass],[Emp_LivroRecUser],[Emp_LivroRecPass] from [dbo].[TBL_MUsers] where Dono_NIF = " + str(n) + "")
    #Texto inicial que queremos que apareça
    json_string = """{"Todos os dados de autenticação onde o Dono_NIF é """ + str(n) + """":["""
    #Os Emp_NIFs e os seus respetivos dados de autenticação
    for row in cursor:
        if row[2] == 'NULL' or 'NoneType':
            row[2] = '-'
        else:
            pass
        if row[3] == 'NULL' or 'NoneType':
            row[3] = '-'
        else:
            pass
        if row[4] == 'NULL' or 'NoneType':
            row[4] = '-'
        else:
            pass
        if row[5] == 'NULL' or 'NoneType':
            row[5] = '-'
        else:
            pass
        if row[6] == 'NULL' or 'NoneType':
            row[6] = '-'
        else:
            pass
        if row[7] == 'NULL' or 'NoneType':
            row[7] = '-'
        else:
            pass
        if row[8] == 'NULL' or 'NoneType':
            row[8] = '-'
        else:
            pass
        if row[9] == 'NULL' or 'NoneType':
            row[9] = '-'
        else:
            pass
        if row[10] == 'NULL' or 'NoneType':
            row[10] = '-'
        else:
            pass
        if row[11] == 'NULL' or 'NoneType':
            row[11] = '-'
        else:
            pass
        if row[12] == 'NULL' or 'NoneType':
            row[12] = '-'
        else:
            pass
        if row[13] == 'NULL' or 'NoneType':
            row[13] = '-'
        else:
            pass
        if row[14] == 'NULL' or 'NoneType':
            row[14] = '-'
        else:
            pass
        if row[15] == 'NULL' or 'NoneType':
            row[15] = '-'
        else:
            pass
        if row[16] == 'NULL' or 'NoneType':
            row[16] = '-'
        else:
            pass
        if row[17] == 'NULL' or 'NoneType':
            row[17] = '-'
        else:
            pass
        if row[18] == 'NULL' or 'NoneType':
            row[18] = '-'
        else:
            pass
        if row[19] == 'NULL' or 'NoneType':
            row[19] = '-'
        else:
            pass
        if row[20] == 'NULL' or 'NoneType':
            row[20] = '-'
        else:
            pass
        if row[21] == 'NULL' or 'NoneType':
            row[21] = '-'
        else:
            pass
        if row[22] == 'NULL' or 'NoneType':
            row[22] = '-'
        else:
            pass
        if row[23] == 'NULL' or 'NoneType':
            row[23] = '-'
        else:
            pass
        if row[24] == 'NULL' or 'NoneType':
            row[24] = '-'
        else:
            pass
        if row[25] == 'NULL' or 'NoneType':
            row[25] = '-'
        else:
            pass
        json_string = json_string + """{"Emp_NIF": '""" + row[0] + """'; "Emp_Empresa": '""" + row[1] +  """; "Emp_UserAT": '""" + row[2] + """'; "Emp_PasswordAT": '""" + row[3] + """'; "Emp_UserSS": '""" + row[4] + """'; "Emp_PasswordSS": '""" + row[5] +"""'; "Emp_IAPMEIUser": '""" + row[6] + """'; "Emp_IAPMEIPass": '""" + row[7] + """'; "Emp_RelUnicoUser": '""" + row[8] + """'; "Emp_RelUnicoPass": '""" + row[9] + """'; "Emp_INEUser": '""" + row[10] + """'; "Emp_INEPass": '""" + row[11] + """'; "Emp_IEFPUser": '""" + row[12] + """'; "Emp_IEFPPass": '""" + row[13] + """'; "Emp_IEFPOnlineUser": '""" + row[14] + """'; "Emp_IEFPOnlinePass": '""" + row[15] + """'; "Emp_SILIAMBUser": '""" + row[16] + """'; "Emp_SILIAMBPass": '""" + row[17] + """'; "Emp_SIRAPAUser": '""" + row[18] + """'; "Emp_SIRAPAPass": '""" + row[19] + """'; "Emp_B2020User": '""" + row[20] + """'; "Emp_B2020Pass": '""" + row[21] + """'; "Emp_SoftFaturacaoUser": '""" + row[22] + """'; "Emp_SoftFaturacaoPass": '""" + row[23] + """'; "Emp_LivroRecUser": '""" + row[24] + """'; "Emp_LivroRecPass": '""" + row[25] + """'}"""
    #Fechamos o texto json
    json_string = json_string + """]}"""
    #print(json_string)
    return json_string

#Chamar a função
#Autenticacoes('502793481')
