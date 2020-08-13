#Ligação à base de dados e visualização da tabela.
#Também posso eliminar valores da tabela

#Módulos
import pyodbc

#Ligação à base de dados
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-TN8OGODS;"
    "Database=Dados;"
    "Trusted_Connection=yes;"
)

#Função Ler
def read(conn):
    cursor = conn.cursor()
    cursor.execute("select * from dados")
    for row in cursor:
        Número = row[0]
        Nome = row[1]
        Apelido = row[2]
        #Imprimir texto + elementos da tabela
        print("Número                                             Nome e Apelido")
        print (row[0],row[1], row[2],)
    #Retornar a/as colunas
    return (Número, Nome, Apelido)

#Eliminar valores da tabela
#def delete(conn):
#    cursor = conn.cursor()
#    cursor.execute(
#       'delete from dados where Nome = Maria'
#    )
#    conn.commit()
 
#delete(conn)

#Indicação da conecção da função read(Ler)
read(conn)
#Fechar a conecção
conn.close()