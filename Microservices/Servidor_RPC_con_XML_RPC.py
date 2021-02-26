#Link do video-> https://www.youtube.com/watch?v=BvUpPeXsOoI

#NOTAS:Para executar os metodos rpc tenho de ir ao PyCharm -> View -> Tool Windows -> Python Console
#Depois tenho de escrever -> from xmlrpc.client import ServerProxy
#Em seguida indico um nome qualquer aqui vou usar o s e indico o url que vou usar -> s = ServerProxy('http://localhost:20064', allow_none=True)
#Executar metodos
#Adicionar chaves e elementos -> s.set('lenguaje','Python') -> lenguaje é a chave, Python é o elemnto
#Visualizar todas as chaves -> s.keys()
#Verificar se um elemento existe -> s.exists('Python) -> Se o elemento existir o programa retorna "True", se o elemento não existir retorna "False"

#Módulos
from xmlrpc.server import SimpleXMLRPCServer

class RPC:
    _methodos_rpc = ['get','set','delete','exists','keys']

    def __init__(self,direccion):
        self._datos = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._methodos_rpc:
            self._servidor.register_function(getattr(self,metodo))
        
    def get(self,nombre):
        return self._datos[nombre]
    
    def set(self,nombre,valor):
        self._datos[nombre] = valor

    def delete(self,nombre):
        del self._datos[nombre]

    def exists(self,nombre):
        return nombre in self._datos
    
    def keys(self):
        return list(self._datos)
    
    def iniciar_servidor(self):
        self._servidor.serve_forever()
    
if __name__ == '__main__':
    rpc = RPC(('',20064))
    print('Se ha iniciado el servidor RPC')
    rpc.iniciar_servidor()