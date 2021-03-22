#Testes da aplicação API
#NOTA:Para realizar um teste, na função tenho de iniciar o nome com test_
#def test_Nome():

#Módulos
import base64
import unittest
#Ficheiro API
from API import *

#Retorna a autorização header
def auth_header(username, password):
    credentials = f'{username}:{password}'
    b64credentials = base64.b64encode(credentials.encode()).decode('utf-8')
    return {'Authorization': f'Basic {b64credentials}'}


class TestAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        pass
    
    #Credenciais corretas
    def test_Credenciais_Corretas(self):
        credentials = auth_header('502793481', '269215474901')
        res = self.client.get('http://127.0.0.1:5000/download/DUC/502793481/2016/12', headers=credentials)
        self.assertEqual(res.status_code, 200)

    #Credenciais incorretas
    def test_Credenciais_Erradas(self):
        credentials = auth_header('no-user', 'no-password')
        res = self.client.get('http://127.0.0.1:5000/download/DUC/502793481/2016/12', headers=credentials)
        self.assertEqual(res.status_code, 403)

    #Não autenticado
    def test_Nao_Autenticado(self):
        credentials = auth_header('', '')
        res = self.client.get('http://127.0.0.1:5000/download/DUC/502793481/2016/12', headers=credentials)
        self.assertEqual(res.status_code, 401)

    #Página não encontrada/Link incorreto
    def test_Not_found(self):
        credentials = auth_header('502793481', '269215474901')
        res = self.client.get('http://127.0.0.1:5000/download/DUC/502793481/2016/', headers=credentials)
        self.assertEqual(res.status_code, 404)

#Iniciar o unitest
if __name__ == '__main__':
    unittest.main()