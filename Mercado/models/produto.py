#Módulos
#Importaçção de Ficheiros
from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1
    #Gerar o código
    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    #Propriedades
    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    #Retorna as informações do produto
    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.preco)}'