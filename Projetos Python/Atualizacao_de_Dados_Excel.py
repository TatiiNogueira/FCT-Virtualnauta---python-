#Separar dois nomes que estão na mesma célula de uma coluna de um fichiero excel
#Criar duas colunas no qual serão inseridos os nomes e colucar os dados atualizados num novo ficheiro excel

#Módulos
import pandas as pd

#Ficheiro Excel
excel = 'Excel.xlsx'

#Ler os ficheiros Excel, sheet_name é o nome da folha excel
first_shift = pd.read_excel(excel, sheet_name='Clean')

#Imprimir número expecifico de linhas do ficheiro excel
print(first_shift.head(5))

#Apenas para fazer uma separação entre as tabelas
print("............................................")

#Separar o Primeiro e o último nome
First_Names_List = []
Last_Names_List = []

#Indicação da coluna onde estão os nomes
excel_names = first_shift['Name, Last Name']
#Imprimimos a coluna para verificar que está tudo bem
print(excel_names)

#Apenas para fazer uma separação entre as tabelas
print("............................................")

#Criação do Loop que irá pegar na coluna do excel que contem os nomes
#E irá fazer a separação do nome e do apelido
#Se quiser que os valores apareçam em letra maiúscula basta escrever .upper() à frente dos valores
#Neste caso poderia colcar à frente de "First_Name" e "Last_Name"
for name in excel_names:
    #Entre '' fica o que separa os dois nomes neste caso espaço
    First_Name, Last_Name = name.split(' ',1)
    #Coloco os nomes dentro da lista de nomes que está vazia
    First_Names_List.append(First_Name)
    #Coloco os sobrenomes dentro da lista de sobrenomes que está vazia
    Last_Names_List.append(Last_Name)

#Imprimimos os nomes e os apelidos para verificar que correu bem
print(First_Names_List, "\n", Last_Names_List)
print("............................................")

#Criar uma coluna para os nomes e outra para os apelidos e colocar no ficheiro excel
#Temos de indicar a posição onde queremos que as colunas fiquem, o nome para a coluna e os valores(Nomes e os Apelidos)
first_shift.insert(0, "First Name", First_Names_List)
first_shift.insert(1, "Last Name", Last_Names_List)
#Eliminar a coluna que tem os nomes e os sobrenomes
del first_shift['Name, Last Name']

#Imprimir o fichiero excel
print(first_shift)

#Criar um ficheiro excel com os dados atualizados
first_shift.to_excel("Atualização de dados.xlsx")