#Módulos
from typing import List, Dict
from time import sleep
#Importação dos Ficheiros
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

#Menu com as opções
def menu() -> None:
    print('*********************************************************')
    print('******************* 😽 Bem-vindo(a) 😽 *******************')
    print('*******************   😽 Shop 😽       *******************')
    print('*********************************************************')

    print('Indique uma das opções abaixo: ')
    print('1 - Registar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Concluir Pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input("Opção nº: "))

    #Opções
    if opcao == 1:
        registar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        concluir_pedido()
    elif opcao == 6:
        print("Volte sempre 🙋")
        #Tempo de espera em segundos
        sleep(2)
        exit(0)
    else:
        print("Opção inválida")
        #Tempo de espera em segundos
        sleep(1)
        menu()

#Função Registar o produto
def registar_produto() -> None:
    print("Registo do Produto")
    print("**************************")

    #Pedir o nome do produto e o seu respetivo preço
    nome: str = input("Indique o nome do produto: ")
    preco: float = float(input("Indique o preço do produto: "))

    produto: Produto = Produto(nome,preco)

    #Adicionar o novo produto à nossa lista de produtos
    produtos.append(produto)

    print(f'O produto {produto.nome} foi registado com sucesso')
    # Tempo de espera em segundos
    sleep(2)
    menu()

#Função que lista os produtos
def listar_produtos() -> None:
    if len(produtos) > 0:
        print('*************************')
        print('Listagem de produtos')
        print('*************************')
        for produto in produtos:
            print(produto)
            print("****************")
            sleep(1)
    else:
        print("Ainda não existem produtos registados")
    sleep(2)
    menu()

#Função Comprar produto
def comprar_produto() -> None:
    if len(produtos) > 0:
        print("******************** Produtos Disponiveis *********************")
        for produto in produtos:
            print(produto)
            print("********************************************************")
            # Tempo de espera em segundos
            sleep(1)
        codigo: int = int(input("Indique o código do produto que deseja adicionar ao carrinho: "))
        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_Carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        # Tempo de espera em segundos
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adiconado ao carrinho.')
                    #Tempo de espera em segundos
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                # Tempo de espera em segundos
                sleep(2)
                menu()
        else:
            print(f"O produto com código {codigo} não foi encontrado.")
            #Tempo de espera em segundos
            sleep(2)
            menu()

    else:
        print("Ainda não existem produtos para vender.")
    sleep(2)
    menu()

#Função que mostra os itens do carrinho
def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print("Produtos no carrinho")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print("******************************")
                sleep(1)
    else:
        print("Ainda não existem produtos no carrinho")
    sleep(2)
    menu()

#Função que faz a finalização do produto
def concluir_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print("Produtos do Carrinho")
        #Lista dos produtos
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                #Soma dos preços
                valor_total += dados[0].preco * dados[1]
                print("************************************")
                sleep(1)
        print(f'O seu recibo é {formata_float_str_moeda(valor_total)}')
        print("Obrigada por fazer compras conosco 😃")
        print("🙋 Volte sempre 🙋")
        #Limpar todos os itens do carrinho
        carrinho.clear()
        sleep(5)
    else:
        print("Ainda não existem produtos no carrinho")
    #Tempo de espera em segundos
    sleep(2)
    menu()

#Função que procura o produto através do código (Esse código é único)
def pegar_produto_por_codigo(codigo: int) -> None:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

#Inicializar o programa
if __name__ == '__main__':
    main()