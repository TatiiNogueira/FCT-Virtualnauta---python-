#Módulos
import torch

#Retorna tensor([1., 1., 1., 1., 1.])
a = torch.ones(5)
print(a)
#Onde está o zero colocamos o valor que queremos (0->Primeiro Valor, 1->Segundo Valor ...),
#mas o valor tem de ser sempre inferior ao indicado no anterior que neste caso é 5
#ou seja neste caso pode ser até ao 4
print(a[0])
#Podemos indicar de que valor a valor queremos ver
print(a[0:3])
#Retorna o valor com casas decimais neste caso o valor é (1.) que será "convertido" para 1.0
print(float(a[1]))
#Substiruir um valor
a[0] = 5.0
print(a)
#Saber o número de valores, o resultado aparece torch.Size([5]), onde está o 5 é o número de valores
print(a.size())
#saber o número de linhas
print(a.dim())
#Mostra cada valor numa linha e mostra o valor.0
print(a.storage())
#Números binários(0,1) aleatórios
print(a.bernoulli_())
#Saber o dtype
print(a.dtype)

#Fazer com que todos os valores sejam zero, o 5 é o número de valores
b = torch.zeros(5)
print(b)

#Gerar números automáticamente/aleatórios, 5 é o número de linhas, 3 número de valores por linha
c = torch.empty(5,3)
print(c)

#Gerar números automáticamente/aleatórios começados por zero
#(número de linhas, número de valores por linha) por exemplo(5,5)
#A saída dos valores é bidimensional
d = torch.rand(5,5)
print(d)

#Depois de torch. colocamos o tipo de dados que queremos neste caso longos(long)
#(número de linhas, número de valores por linha) por exemplo(5,5)
e = torch.ones(5,5, dtype= torch.long)
print(e)

#Depois de torch. colocamos o tipo de dados que queremos neste caso inteiros 32(int32) - Coloca os valores em inteiros
#(número de linhas, número de valores por linha) por exemplo(5,5)
#Quando imprimimos os valores aparece no final dtype=torch.int32
f = torch.ones(5,5, dtype= torch.int32)
print(f)

#Introduzimos os valores floats que queremos(valores decimais)
#E o programa coloca os valores com 4 casas depois da virgula
g = torch.tensor([5.5, 15.5])
print(g)

#Depois de torch. colocamos o tipo de dados que queremos
#(número de linhas, número de valores por linha) por exemplo(5,3)
#Quando imprimimos os valores aparece no final dtype=torch.float64  
h = torch.ones(5,3, dtype= torch.double)
print(h)

#2D - Os valores ficam sem o zero
i = torch.tensor([[5.0,6.0],[8.0,9.0],[11.0,12.0]])
print(i)
#Saber o número de linhas e o número de valores por linha
print(i.shape)
print(i.size())

j = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
#Média
print(torch.mean(j))
#Valor que fica no meio
print(torch.median(j))
#Desvio padrão
print(torch.std(j))
#Variancia
print(torch.var(j))

#Retorna tudo 0, mas na diagonal retorna 1. ou seja
#O 1. vai aparecer no 1º valor da 1ª linha, no 2º valor da 2ª linha ....
#Os outros valores serão 0.
#5 é o número de linhas e valores por linha, 
m = torch.eye(5)
print(m)

#Atribuir nome a um Tensor, o nome é atribuido a cada linha
#Se não quiser atribuir um nome a uma ou mais linhas, ao invés de escrever o nome da linha escrevo NULL
#(número de linhas, número de valores por linha) por exemplo(2,3)
n = torch.zeros(2,3, names= ("A", "B"))
print(n)