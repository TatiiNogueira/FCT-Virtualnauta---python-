#Módulos
import torch

a = torch.ones(3,2)
print(a)
b = torch.ones(3,2)
k = torch.tensor([1,2,3,4,5])
l = torch.tensor([6,7,8,9,10])

#Divisão, para fazer uma divisão não posso usar valores do tipo Longo(type Long)
print(a.div_(b))

#Exponente
print(a.exp_())

#Cosseno
print(a.cos_())

#Maneira 1
#Soma
print(k + l)
#Subtração
print(k-l)
print(l-k)
#Multiplicação
print(k * l)

#Maneira 2
#Soma
print(k.add_(l))
#Subtração 
print(k.sub_(l))
print(l.sub_(k))
#Multiplicação
print(k.mul_(l))