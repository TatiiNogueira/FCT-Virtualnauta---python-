#Pergunta com resposta de Sim ou Não
def perg_ok(perg, tentativas = 3, lembrete = 'Responda Sim ou Não'):
    while True:
        ok = input(perg)
        if ok in ('s', 'S', 'Sim', 'sim','SIM'):
            return True
        if ok in ('n', 'nao', 'N', 'Nao', 'NAO', 'não', 'NÃO'):
            return False
        tentativas = tentativas - 1
        if tentativas < 0:
            raise ValueError('Resposta inválida')
        print(lembrete)

if perg_ok('Deseja continuar ? ') != True:
    print('Código terminado')
else:
    print('Código continuado')
