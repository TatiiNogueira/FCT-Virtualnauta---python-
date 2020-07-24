PARTE 1

Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Tutorial
>>> #Contas - Para fazermos contas não é preciso fazer espaços
>>> 5+5
10
>>> 5 + 5
10
>>> 5*5
25
>>> 5-5
0
>>> 5/5
1.0
>>> 5/6
0.8333333333333334
>>> 5+10 #Resultado = 10 (Posso escrever o comentário onde quiser pois ele não irá afetar em nada1)
15
>>> 5.8+4.0
9.8
>>> 5.8+4
9.8
>>> #As regras da matemáticas são aplicadas ou seja os parenteses tem perioridade, depois a multiplicação e a divisão e só no fim é que é a soma e a subtração
>>> 10+10*2
30
>>> (10+10)/2
10.0
>>> #Fazer com que uma conta de divisão dê valores inteiros
>>> #O que acontece é que o valor ignora a parte decimas ficando apenas o/os valor/s antes da vírgula
>>> 17/3
5.666666666666667
>>> 17//3
5
>>> #Valor com potência
>>> #É como se o 5 estive elevadon a dois ou seja é o mesmo que 5*5=25
>>> 5**2
25
>>> #Saber o resto de uma divisão ao invés de colocar o sinal da divisão colocamos %
>>> 17%3
2
>>> tati =10
>>> tati
10
>>> sofia=20
>>> sofia
20
>>> tati+sofia
30
>>> #Isto foi uma variavel, atribui um nome a um valor ao escrever tati+sofia é o mesmo que tive se escrito 10+20
>>> #Soma de uma variavel (tati) mais uma variavel que não defini (oscar), isto irá dar erro
>>> tati+oscar
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tati+oscar
NameError: name 'oscar' is not defined
>>> oscar=30
>>> tati+oscar
40
>>> #Fazer uma conta com o valor anterior
>>> 5+10*2.5
30.0
>>> 20+_
50.0
>>> #Colocar um valor/conta decimal apenas com duas casas decimais
>>> 17/3
5.666666666666667
>>> round(17/3)
6
>>> #Conta anterior errada, enganei me
>>> round(17/3,2)
5.67
>>> #Strings
>>> "Exemplo 1"
'Exemplo 1'
>>> 'Exemplo2'
'Exemplo2'
>>> "Exemplo'3"
"Exemplo'3"
>>> 'Exemplo"número4"'
'Exemplo"número4"'
>>> print('Exemplo5 - Mais Bonito')
Exemplo5 - Mais Bonito
>>> 'Don\'t eat exemplo6'
"Don't eat exemplo6"
>>> "Citação:\"Exemplo7\""
'Citação:"Exemplo7"'
>>> #Exemplo8 - Escrita normal
>>> print('C:\meupc\novo')
C:\meupc
ovo
>>> #Isto acontece porque o \n significa paragrafo para isso não acontecer tenho de usar um r
>>> print(r'C:\meupc\novo')
C:\meupc\novo
>>> #Este r significa escrever tal e qual como está
>>> #Concatenação
>>> 'Concatenação''Exemplo'
'ConcatenaçãoExemplo'
>>> 'Exemplo'+'Melho'
'ExemploMelho'
>>> 'Exemplo ' +'2'
'Exemplo 2'
>>> #Não me posso esquecer de dar um espaço antes da segunda aspa, se não ele irá escrever tudo junto
>>> 5*'Tic'
'TicTicTicTicTic'
>>> 5*'Tic '
'Tic Tic Tic Tic Tic '
>>> 5* 't ' + 'b'
't t t t t b'
>>> #variavel
>>> variavel = 'Sapo'
>>> print(variavel)
Sapo
>>> print('variavel')
variavel
>>> #Apenas letra da variavel
>>> var=conta
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    var=conta
NameError: name 'conta' is not defined
>>> var='conta'
>>> var
'conta'
>>> letra1 =var[0]
>>> letra1
'c'
>>> letra4=var[3]
>>> print(letra4)
t
>>> letra4
't'
>>> #Se quiser que ele comecce a contar pelo fim os números começam pelo -1 porque não existe -0
>>> ultimaletra=var[-2]
>>> ultimaletra
't'
>>> texto='Isto é apenas um Exemplo'
>>> texto
'Isto é apenas um Exemplo'
>>> partedafrase=texto[0:5]
>>> partedafrase
'Isto '
>>> #Utilizar sempre o print quando quero ver o resultado
>>> len(texto)
24
>>> len('texto')
5
>>> #Consertar uma variavel
>>> j='Eu não sei esvver'
>>> j
'Eu não sei esvver'
>>> j=j[:-4] +'c' + j[-3:]
>>> j
'Eu não sei escver'
>>> j=j[:-4] +'re' + j[-3:]
>>> j
'Eu não sei esrever'
>>> #LISTAS
>>> [1,2,3,4,5]
[1, 2, 3, 4, 5]
>>> ['flor','morango']
['flor', 'morango']
>>> Tabuada2=[2,4,6,8,10,12,14,16,18,20]
>>> Tabuada2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> Tabuada2.append(22)
>>> Tabuada2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
>>> letras = ['a','b','c','d']
>>> len(letras)
4
>>> letras + ['e','f','g']
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> a=['a','b','c']
>>> b=[1,2,3]
>>> x=[a,b]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[1][0]
1
........................................................................................................................................................................
PARTE 2

>>> #Atribuir várias variáveis na mesma linha
>>> a,b,c = 1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> a,b,c
(1, 2, 3)
>>> a,c
(1, 3)
>>> b,c
(2, 3)
>>> #Mudança nas variáveis
>>> a,b =b,a+b
>>> a,b
(2, 3)
>>> #Verdadeiro e Falso
>>>#while-Significaa enquanto   break-Significa quebra ou seija parar, se não escrevesse moso break o computador iria escrever infinitamente a palavra/frasee que indicamos
>>> while True:
	print('Falso')
	break
    
>>> while True:
	print('Verdadeiro')
	break

Verdadeiro
#Permitir um certo número de repetição de uma palavra/frase
>>> while True:
	print('Verdadeiro '*5)
	break

Verdadeiro Verdadeiro Verdadeiro Verdadeiro Verdadeiro
#Verdadeiro e falso mas com valores
>>> while 3>4:
	print('a')
	break

>>> while 3<4:
	print('b')
	break

b
#Quando usamos o sinal de mais temos de ter atenção pois
# = Significa atribuiição que é usado nas variáveis
# == Significa igualdade
>>> while 3==4:
	print('c')
	break

>>> while 4==4:
	print('c')
	break

c
.......................................................................................................................................................................
PARTE3

>>> while 8!=3:
	print('Confirmado')
	break

Confirmado
>>> while 8!=8:
	print('Como é falso não escreve nada')
	break

>>> #Se eu escrever apenas os valores o computador apenas irá dizer se a afirmação é verdadeira ou falsa
>>> 8!=3
True
>>> 8!=8
False
>>> 5==5
True
>>> 4+5<3+7
True
>>> 3+3<4+2
False
>>> #Verdadeiro e Falso usando variáveis
>>> a = 2
>>> b = 5
>>> c = b > 7
>>> c
False
>>> c = a != b
>>> c
True
>>> d = 1
>>> while d<5:
	print(d)
	d = d + 1

	
1
2
.................................................................................................................................................................................
PARTE 4

>>> #Usando o if
>>> if True:
	print('Testando o if')

	
Testando o if
