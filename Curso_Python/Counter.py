#Notas
#A lista aperece do elemento com mais vezes repetidas para o elemento com menos vezes repetidas

#Módulos
from collections import Counter

#Exemplo 1
#Podemos usar qualquer iterável, neste caso uma lista
lista = [1,1,1,2,2,3,3,3,4,4,4,4,55,55,5]

#Utilizando o Counter
res = Counter(lista)

print("\U0001F64C",res)
#Resultado -> Counter({4: 4, 1: 3, 3: 3, 2: 2, 55: 2, 5: 1})
#Primeiro mostra o elemnto e à frente quantos elementos iguais existem

###################################################################################################

#Exemplo 2
#Utilizando uma String
print("\U0001F64C",Counter('Hello'))
#Resultado -> Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
#Mostra o número de vezes que cada letra é repetida

###################################################################################################

#Exemplo 3
#Utilizando um texto longo e separando por palavras
texto = "Python um mundo incrivel. Bem vindo ao mundo de Python"

palavras = texto.split()

a = Counter(palavras)
print("\U0001F64C",a)
#Resultado ->  Counter({'Python': 2, 'mundo': 2, 'um': 1, 'incrivel.': 1, 'Bem': 1, 'vindo': 1, 'ao': 1, 'de': 1})
#Mostra o número de vezes que cada palavra é repetida