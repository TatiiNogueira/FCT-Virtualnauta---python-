#Link do Site -> https://debugeverything.com/programacao-em-python-aplicativo-flask/

#Módulos
from flask import Flask
from flask import jsonify
from flask import render_template
import json

#Inicializar o Flask
app = Flask(__name__, template_folder='.')

#Definir as rotas
#Para ver o resultado tenho de escrever o URL na aplicação do Postman e indicar o "methods" que é o método
#E o programa precisa de estar a correr para podermos ver os resultados
@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return render_template('tasks.json')

@app.route('/todo/create',methods=['POST'])
def createTask():
    return 'Create new task'

@app.route('/todo/update',methods=['UPDATE'])
def updateTask():
    return 'Update Task'

@app.route('/todo/delete',methods=['DELETE'])
def deleteTask():
    return 'Delete task'

#Dá nos o URL do nosso site
if __name__ == '__main__':
    app.run(debug=True)