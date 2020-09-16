#Criar ficheiro json
#json = java script object notation seializer

#Módulos
import json

#Criação de um dicionário
data = {'Nome': 'Pedro', 'RG' : 123456789, 'CPF' : 123456789}
#Converter o dicionário numa string
data_string = json.dumps(data)

#Criar arquivo, inserir informação e fechar
file = open('Criar_Ficheiro_json.json', 'w')
file.write(data_string)
file.close()