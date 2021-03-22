#NOTA: n  é o ID que nós introduzimos

#Módulos
from flask import Flask, render_template, make_response, jsonify, request,Response
from flask_cors import CORS
import base64
import json
#Importação os ficheiros
from Titulo import *
from Categoria import *
from Data import *
from Descricao import *
from Grador import *
from Sala import *
from Todos import *
from Inserir import * 
from Delete import * 
from Todos_Valores import * 

#Inicializar o Flask
app = Flask(__name__, template_folder='.')
CORS(app)

#Definir as rotas
#Para ver o resultado tenho de escrever o URL na aplicação do Postman e indicar o "methods" que é o método
#E o programa precisa de estar a correr para podermos ver os resultados
#Funções pra ver os dados em separado
#Coluna Titulo
@app.route('/get/Titulos/<int:n>/',methods=['GET'])
def getTitulos(n):
    data = {}
    data['Titulos'] = Titulos(n)
    return Response(Titulos(n),mimetype='application/json')

#Coluna Grador
@app.route('/get/Gradadores/<int:n>/',methods=['GET'])
def getGradadores(n):
    data = {}
    data['Gradadores'] = Gradores(n)
    return Response(Gradores(n),mimetype='application/json')

#Coluna Categoria
@app.route('/get/Categorias/<int:n>/',methods=['GET'])
def getCategorias(n):
    data = {}
    data['Categorias'] = Categorias(n)
    return Response(Categorias(n),mimetype='application/json')

#Coluna Descricao
@app.route('/get/Descricoes/<int:n>/',methods=['GET'])
def getDescricoes(n):
    data = {}
    data['Descricoes'] = Descricoes(n)
    return Response(Descricoes(n),mimetype='application/json')

#Coluna Data
@app.route('/get/Datas/<int:n>/',methods=['GET'])
def getDatas(n):
    data = {}
    data['Datas'] = Datas(n)
    return Response(Datas(n),mimetype='application/json')

#Coluna Sala
@app.route('/get/Salas/<int:n>/',methods=['GET'])
def getSalas(n):
    data = {}
    data['Salas'] = Salas(n)
    return Response(Salas(n),mimetype='application/json')

#Vai à pasta Fotos e codifica em base64 a imagem desejada
@app.route('/get/ImagensID',methods=['GET'])
def getImagensID():
    data = {}
    #Abrir e ler a imagem
    with open('Fotos/Primeira.png', mode='rb') as file:
        img = file.read()
    #Codificar e retorna a imagem em base64
    data['img'] = base64.encodebytes(img).decode('utf-8')
    return Response(json.dumps(data), 200, mimetype='application/json')

#Ver todos os valores de uma linha
@app.route('/get/Todos/<int:n>/',methods=['GET'])
def getTodos(n):
    data = {}
    data['Todos'] = Todos(n)
    return Response(Todos(n),mimetype='application/json')

#Ver todos os Valores da tabela
@app.route('/TodosValores',methods=['GET'])
def getTodosRegistos():
    data = {}
    data['Todos os Valores'] = TodosValores()
    return Response(TodosValores(),mimetype='application/json')

#Função para inserir os dados
#Para inserir os dados tenho de ir ao PostMan, clico em Body, seleciono a opção raw,
#escrevo a json_string que está no ficheiro Inserir.py e substituo as letras pelos dados que eu quero
#EX: {"Titulo":"12","Grador":"Maria","Categoria": "A", "Descricao": "Reprovado","Data": "2020-01-01 00:00:00", "Sala": "2", "ImagemID": "2"}
@app.route('/Inserir',methods=['PUT', 'POST'])
def Inserir():
    content = request.json
    print(content)
    a = content["Titulo"]
    b = content["Grador"]
    c = content["Categoria"]
    d = content["Descricao"]
    e = content["Data"]
    f = content["Sala"]
    g = content["ImagemID"]
    INSERE(a,b,c,d,e,f,g)
    return make_response(jsonify(), 200)

#Função para eliminar os dados de uma linha da tabela
@app.route('/Delete/<int:n>/',methods=['DELETE'])
def Delete(n):
    DELETE(n)
    return make_response(jsonify(), 200)

#Função que permite realizar as três ações
#Permite ver todos os elementos de uma linha da tabela, Introduzir valores na tabela ou eliminar uma linha da tabela
#Utilizando o mesmo link mas indicando o médoto "methods"(GET,POST,PUT,DELETE), que é o que os vai diferenciar
@app.route('/Tudo/<int:n>/',methods=['GET', 'POST', 'PUT', 'DELETE'])
def Todasasfuncoes(n):
    #Ver todos os elementos de uma linha da tabela
    if request.method == 'GET':
        data = {}
        data['Todos'] = Todos(n)
        return Response(Todos(n),mimetype='application/json')
    #Introduzir dados na tabela
    #Quando colocar o link tenho de colocar um ID(número) qualquer não irá afetar em nada,
    #posso até mesmo colocar um que não exista
    elif request.method == 'POST' or 'PUT':
        Inserir()
        return make_response(jsonify(), 200)
    #Eliminar uma linha da tabela
    else:
        Delete(n)
        return make_response(jsonify(), 200)

#Dá nos o URL do nosso site
if __name__ == '__main__':
    app.run(debug=True)