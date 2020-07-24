#Depois de feita a instalação no cmd.
#Imporatamos o pyodc para aqui
import pyodbc

#Função Ler
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from dummy")
    for row in cursor:
        print(f'row = {row}')
    print()

#Função Crear
def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'insert into dummy(a,b) values(?,?);',
        (3232, 'catzzz')
    )
    conn.commit()
    read(conn)

#Função Atualizar
def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'update dummy set b = ? where a = ?;',
        ('dogzzz', 3232)
    )
    conn.commit()
    read(conn)

#Função Eliminar
def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        'delete from dummy where a > 5'
    )
    conn.commit()
    read(conn)    

#Definimos que a ligação será igual ao pyodbc
#Colocamos a String que é a Driver
#Indicamos o nome do nosso servidor (Apenas o que vem antes do parenteses)
#Indicamos o nome da database a ser usada
#Indicamos que é uma ligação confiável
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-TN8OGODS;"
    "Database=Conect;"
    "Trusted_Connection=yes;"
)

#Indicação de que quero fazer uma conecção com
#a base de dados para cada funçã o definida a seguir
read(conn)
create(conn)
update(conn)
delete(conn)
#Após feito o que está indicado anteriormente
#Indicamos que fechamos a conecção
conn.close()