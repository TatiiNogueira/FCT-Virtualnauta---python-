#Módulos
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['Curso'] = 'Programação em Python: Essencial'

print('\U0001F680',dicionario)
#Como dicionario['Outro'] não existe o programa imprime 0
#Ao invés de dar KeyError
print('\U0001F680',dicionario['Outro'])
print('\U0001F680',dicionario['Curso'])