#Exemplo 1
paises = ["","Russia","","Angola","","Mexico"]
print(paises)

#Mostrar os valores que não são None\Vazios
res =  filter(None, paises)
print(list(res))

#OU

res = filter(lambda paises: paises != '', paises)
print(list(res))

#OU
res = filter(lambda paises: len(paises) > 0, paises)
print(list(res))

##################################################################

#Exemplo 2
usuarios = [
    {"username": "Samuel", "tweets" : ["Eu adoro bolos", "Eu adoro piza"]},
    {"username": "Carla", "tweets" : ["Eu odeio morangos"]},
    {"username": "Paulo", "tweets" : []},
    {"username": "Maria", "tweets" : []},
    {"username": "João", "tweets" : ["Eu adoro jogar andebol", "Eu adoro naa no lago"]},
    {"username": "Amélia", "tweets" : []}
    ]

print(usuarios)

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)