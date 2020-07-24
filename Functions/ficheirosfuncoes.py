                    #LER ARQUIVOS

#Criamos uma variavel e dentro dessa variável indicamos que
#Desejamos abrir o ficheiro,
#e apenas podemos ler não podemos alterar nenhuma informação
employees_file = open("employees.txt", "r")

#Ler uma linha em especifico, tenho de indicar a posição
#a posição fica onde se encontra o número 1
#a contagem começa pelo zero
#print(employees_file.readlines()[1])

#Apenas ler o ficheiro
#print(employees_file.read())

#Ler cada linha de empregado em separado
for employee in employees_file.readlines():
    print(employee)

#Fechar o ficheiro
employees_file.close()

                #ESCREVER UM ELEMENTO NOVO DO FINAL DO ARQUIVO
#employees_file = open("employees.txt", "a")
#Adicionar um novo elemento a um ficheiro no final do ficheiro
#Cada vez que eu colocar o programa para correr ele irá criar novamente
#o elemento que eu escrevi
#employees_file.write(("\nAndreia - Secretaria"))
#employees_file.close()

                #REESCREVER UM FICHEIRO
#employees_file = open("employees.txt", "w")
#Iria eliminar tudo o que se encontrava no meu arquivo e iria
#apenas escrever o que eu indiquei
#employees_file.write("Raquel - Administracion")
#employees_file.close()

            #CRIAR UM NOVO FICHEIRO
#Criar um ficheiro por exemplo em HTML
employees_file = open("index.html", "w")
employees_file.write("<p>This is a pag HTML</p>")
employees_file.close()
