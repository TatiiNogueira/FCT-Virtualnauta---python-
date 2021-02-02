#NOTA: Só funciona com ficheiros HTML
#Escrevo no campo de busca do google "http://localhost:8080/" + Nome do ficheiro html po exemplo "home.html"
#Completo ficaria assim "http://localhost:8080/home.html"

#Módulos
from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    #Procura pelo ficheiro home.html, que contém a página inicial
    def do_GET(self):
        #Se escrevermos no campo de busca do Browser "localhost:8080/" vai ser o mesmo que "localhost:8080/home.html"
        if self.path == '/':
            self.path = '/home.html'
        #Experimenta abrir o ficheiro
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        #Se não conseguir abrir o ficheiro, irá mostrar a mensagem ERRO, quando tentarmos abrir a página no Browser
        except:
            #Mensagem de erro que aparce na página
            file_to_open = "Page not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

#Número da porta do servidor, posso escolher o que quiser
httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
