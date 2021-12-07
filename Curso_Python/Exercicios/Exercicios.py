print("Exercicio 1")
numeros = {x * 2 for x in range(10)}
print(numeros)

#Faça uma alteração na estrutura a cima para gerar um dicionário ao invés do set

numbers = {x: x ** 2 for x in range(10)}
print(numbers)
letras = {letra for letra in 'Geek University'}
print(letras)

####################################################################

print("Exercicio 2")
#Combinar filter() e map()
nomes = ['Vanessa','Ana','Maria']

#Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que o nome tenha no máximo 5 letras
instrutoras = list(map(lambda nome: f'A tua instrutora é {nomes}', filter(lambda nome: len(nome) < 5, nomes)))
print(instrutoras)

####################################################################

print("Exercicio 3")
#Impimir apenas o titulo da música mais tocada e menos tocada
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2}, 
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock in rool, too young to die", "tocou": 32}
] 

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

####################################################################

print("Exercicio 4")
#Encontrar a música mais tocada e a menos tocada sem usar max(), min() ou  lambda
musicas = [ 
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock in rool, too young to die", "tocou": 32}
]

max = 0 
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])