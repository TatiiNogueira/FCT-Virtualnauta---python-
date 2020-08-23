#Criar ficheiro CSV

#Atribuição de um nome para o arquivo csv
filename = "Ficheiro.csv"
#Cabeçado do ficheiro csv (Não pode conter acentos)
text = "Isto e um fichiero CSV \nCriado atraves de Python"

#Abrir o ficheiro e escrever
file = open(filename, "w")
#Introduzir texto
file.write(text)

#Fechar o ficheiro
file.close()