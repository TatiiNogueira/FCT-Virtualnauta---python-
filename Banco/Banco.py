#Módulos
from typing import List
from time import sleep
#Importação dos Ficheiros
from models.client import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print("-------------------------------------------")
    print("---------------- Banco --------------------")
    print("-------------------------------------------")
    print("Opções")
    print("1 - Criar uma conta")
    print("2 - Efetuar retirada")
    print("3 - Efetuar Depósito")
    print("4 - Efetar Transferência")
    print("5 - Listar contas")
    print("6 - Sair")

    opcao: int = int(input("Indique o número da opção que deseja: "))

    #Opções
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_retirada()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Volte sempre")
        #Tempo de espera
        sleep(2)
        exit(0)
    else:
        print("Opção inválida, tente novamente")
        #Tempo de espera
        sleep(2)
        menu()

def criar_conta() -> None:
    print("Indique os seus dados")
    #Informações pedidas do cliente
    nome: str = input("Nome: ")
    email: str = input("Email:")
    cpf: str = input("CPF: ")
    data_nascimento: str = input("Data de Nascimento: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta : Conta = Conta(cliente)

    #Adicionar a nova conta à lista das conas já existentes
    contas.append(conta)

    print("Conta criada com sucesso")
    print("Dados da Conta")
    print("-------------------------------")
    #Imprimir os dados da conta criada
    print(conta)
    #Tempo de espera
    sleep(2)
    #Voltar para o menu
    menu()

def efetuar_retirada() -> None:
    if len(contas) > 0:
        numero: int = int(input("Indique o número da sua conta: "))

        conta: Conta = procurar_conta_por_numero(numero)
        print(conta)

        if conta:
            valor: float = float(input("Informe o valor da retirada: "))

            conta.sacar(valor)
        else:
            print(f"Não foi possivel encontrar nemhuma conta com o número {numero} ")
    else:
        print("Ainda não foi criada nenhuma conta")
    #Tempo de espera
    sleep(2)
    #Voltar ao menu
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input("Indique o número da sua conta: "))
        conta: Conta = procurar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Indique o valor do depósito: "))

            conta.depositar(valor)
        else:
            print(f"Não foi possivel encontrar nemhuma conta com o número {numero} ")
    else:
        print("Ainda não foi criada nenhuma conta")
    #Tempo de espera
    sleep(2)
    #Voltar ao menu
    menu()

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input("Indique o número da sua conta: "))
        conta_o: Conta = procurar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input("Indique o número da conta destino: "))
            conta_d: Conta = procurar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input("Indique o valor da transferência"))
                conta_o.transferir(conta_d,valor)
            else:
                print(f'A conta destino com o número {numero_d} não foi encontrada')

        else:
            print(f"Não foi possivel encontrar nemhuma conta com o número {numero_o} ")
    else:
        print("Ainda não foi criada nenhuma conta")
    #Tempo de espera
    sleep(2)
    #Voltar ao menu
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print("Listagem de contas")
        for conta in contas:
            print(conta)
            print("--------------------")
            #Tempo de espera
            sleep(1)

def procurar_conta_por_numero(numero: int) -> Conta:
    c: Conta = numero

    if len(contas) > 0:
        pass
    return c

if __name__ == '__main__':
    main()