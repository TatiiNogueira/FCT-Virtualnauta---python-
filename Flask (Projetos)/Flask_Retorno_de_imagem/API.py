#Módulos
from flask import Flask,render_template,make_response,jsonify,request,Response
from flask import send_file
from werkzeug.security import check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import json
#Importação dos ficheiros
from Emp_NIFs import *
from Autenticacoes import *
from Informacoes import *
from Username_Password import *
from DONOs_NIFs import *
from Status_Saft import *
from Status_DMRAT import *
from File_DMR import *
from File_DUC import *
from File_CMP_DMRAT import *
from File_CMP_DMRSS import *
from File_DRI import *
from File_DD import *
from File_DP_Fundos import *
from File_CMP_M22 import * 
from File_DP_M22 import * 

#Inicializar o Flask
app = Flask(__name__, template_folder='.')
CORS(app)

#Definir as rotas
#Dá nos todos os Emps_NIFs onde o DONO_NIF(n) é igual ao que nós indicarmos
@app.route('/get/Emp_NIFs/<int:n>/',methods=['GET'])
def getEmpsNIFs(n):
    data = {}
    data['Emp_NIFs'] = EmpsNIFs(n)
    return Response(EmpsNIFs(n),mimetype='application/json')

#Vai buscar todos os Emp_NIfs e o seus respetivos dados de autenticação cujo DONO_NIF(n) é igual ao que nós indicarmos
@app.route('/get/Autenticacoes/<int:n>/',methods=['GET'])
def getAutenticacoes(n):
    data = {}
    data['Autenticacoes'] = Autenticacoes(n)
    return Response(Autenticacoes(n),mimetype='application/json')

#Vais buscar todos os Emp_NIfs, o Emp_Empresa e os email cujo DONO_NIF(n) é igual ao que nós indicarmos
@app.route('/get/Informacoes/<int:n>/',methods=['GET'])
def getInformacoes(n):
    data = {}
    data['Informacoes'] = Informacoes(n)
    return Response(Informacoes(n),mimetype='application/json')

#Vai buscar o estado do Ficheiro Saft cujo Saft_NIF(n), SAft_Ano(a) e Saft_Mes(m) é igual ao que nós indicarmos
#Mas só mostra o estado do fichiero se esse Saft_NIF(n) que indicarmos pertencer à empresa que fez o pedido
@app.route('/get/StatusSaft/<int:n>/<int:a>/<int:m>',methods=['GET'])
def getStatusSaft(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o Saft_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse Saft_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = Status_Saft(n,a,m)
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return make_response(jsonify(project), 200)

#Vai buscar o estado do Ficheiro DMRAT cujo DMRAT_Emp_NIF(n), DMRAT_Ano(a) e DMRAT_Mes(m) é igual ao que nós indicarmos
#Mas só mostra o estado do fichiero se esse DMRAT_Emp_NIF(n) que indicarmos pertencer à empresa que fez o pedido
@app.route('/get/StatusDMRAT/<int:n>/<int:a>/<int:m>',methods=['GET'])
def getStatusDMRAT(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o DMRAT_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse DMRAT_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = Status_DMRA(n,a,m)
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return make_response(jsonify(project), 200)

#Faz o download do ficheiro DMR
@app.route('/download/DMR/<int:n>/<int:a>/<int:m>')
def DownloadFileDMR(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o DMRAT_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse DMRAT_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileDMR(n,a,m)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro DUC
@app.route('/download/DUC/<int:n>/<int:a>/<int:m>')
def DownloadFileDUC(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o DMRA_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse DMRA_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileDUC(n,a,m)
        #f = "Caminho" + project
        f = "img.jpg"
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro CMP-DMRAT
@app.route('/download/CMP/DMRAT/<int:n>/<int:a>/<int:m>')
def DownloadFileCMPDMRAT(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o DMRAT_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse DMRAT_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileCMP_DMRAT(n,a,m)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro CMP-DMRSS
@app.route('/download/CMP/DMRSS/<int:n>/<int:a>/<int:m>')
def DownloadFileCMPDMRSS(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o DMRS_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse DMRS_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileCMP_DMRSS(n,a,m)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro DRI
@app.route('/download/DRI/<int:n>/<int:a>/<int:m>')
def DownloadFileDRI(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o DMRS_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse DMRS_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileDRI(n,a,m)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro DD
@app.route('/download/DD/<int:n>/<int:a>/<int:m>')
def DownloadFileDD(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o FC_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse FC_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileDD(n,a,m)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro DP-Fundos
@app.route('/download/DP/Fundos/<int:n>/<int:a>/<int:m>')
def DownloadFileDPFundos(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o FC_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse FC_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileDP_Fundos(n,a,m)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro DP
@app.route('/download/DP/M22/<int:n>/<int:a>')
def DownloadFileDPM22(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o M22_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse M22_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileDP_M22(n,a)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Faz o download do ficheiro DP
@app.route('/download/CMP/M22/<int:n>/<int:a>')
def DownloadFileCMP22(n,a,m):
    #401 - Não autenticado
    if request.authorization.username=="" or request.authorization.password=="":
        return make_response(jsonify(), 401)
    #403 - Não possui autorização
    if not Username_Password(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    #Verificação dos DONOS_NIFS
    #Se os DONOs_NIFs forem diferenteres significa que o M22_NIF(n) indicado não pertence a empresa que fez o
    #pedido logpo o programa não permite ver o estado desse M22_NIF(n)
    if Empresa_cliente(n) != Empresa_Chefe(request.authorization.username,request.authorization.password):
        return make_response(jsonify(), 403)
    else:
        #404 - Not found
        project = getfileCMP_M22(n,a)
        f = "Caminho" + project
        if project is None:
            return make_response(jsonify(), 404)
        else:
            #200 - OK
            return send_file(f,as_attachment=True)

#Dá nos o URL do nosso site
if __name__ == '__main__':
    #O host e a porta são gerados automáticamente
    app.run(debug=True)
    #Definir o host e a porta, depois o link ficaria "http://0.0.0.0:8000"
    #app.run(host='0.0.0.0', port=8000)