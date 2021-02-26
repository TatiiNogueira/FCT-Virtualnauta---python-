#http Get extension

#Link -> https://www.youtube.com/watch?v=0ih4SBxCL3I
#NOTAS: O url será -> http://localhost:8000/ e à frente o que defenirmos na rota
#Para iniciarmos a página que queremos temos de escrever no terminal
#nameko run name_file (Onde está name_file substituimos pelo nome do fichiero que queremos executar)

#Módulos
import json
from nameko.web.handlers import http
    
class HttpService(object):
    name = "multiply_service"

    @http('GET', '/multiply/<int:first>/<int:second>')
    def get_method(self,request,first,second):
        third = int(request.args.get('third',1))
        return json.dumps({'value': first * second * third})