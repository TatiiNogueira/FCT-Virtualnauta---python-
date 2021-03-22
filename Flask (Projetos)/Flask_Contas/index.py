#NOTA: n  é o ID que nós introduzimos

#Módulos
from flask import Flask, render_template, make_response, jsonify, request
import json
#Importar os ficheiros
from Mais import *
from Menos import *
from Vezes import *
from Dividir import *

#Inicializar o Flask
app = Flask(__name__, template_folder='.')

#Definir as rotas
#Para ver o resultado tenho de escrever o URL na aplicação do Postman e indicar o "methods" que é o método
#E o programa precisa de estar a correr para podermos ver os resultados
@app.route('/Mais/<int:n>/',methods=['GET'])
def Mais(n):
    data = {}
    data['Resultado'] = Buscar_Mais(n)
    return make_response(json.dumps(data))

@app.route('/Menos/<int:n>/',methods=['GET'])
def Menos(n):
    data = {}
    data['Resultado'] = Buscar_Menos(n)
    return make_response(json.dumps(data))

@app.route('/Vezes/<int:n>/',methods=['GET'])
def Vezes(n):
    data = {}
    data['Resultado'] = Buscar_Vezes(n)
    return make_response(json.dumps(data))

@app.route('/Dividir/<int:n>/',methods=['GET'])
def Dividir(n):
    data = {}
    data['Resultado'] = Buscar_Dividir(n)
    return make_response(json.dumps(data))

#Dá nos o URL do nosso site
if __name__ == '__main__':
    app.run(debug=True)