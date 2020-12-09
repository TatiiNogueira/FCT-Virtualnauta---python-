#Descida gradiente com autógrado e retropropagação - Utilizando a biblioteca torch
#Link -> https://www.youtube.com/watch?v=E-I2DNVzQLg&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=5

#NOTAS:
#Nos prints quando aparece :.nf - O numero que estiver onde está o n é o número de casas decimais
#O x é diferente de X que é uma matriz(array)
#O y é diferente de Y que é uma matriz(array)
#Na programação para trás, primeiro fazemos um passe para a frente

#Módulos
import torch

#Regressão linear
#Função que faz a combinação de alguns pesos e nossas entradas
#f = w * x
#Exemplo
#f = 2 * x

#O x/y vai ser igual a uma matriz(array) de pontos numpy(np)
#O dtype é o tipo de dados da matriz(array)
X = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
#Como a nosso formula é 2x(f = 2 * x) a matriz de y tem de ser os valores da matriz de x vezes 2
Y = torch.tensor([2, 4, 6, 8], dtype=torch.float32)

#Inicializamos, para isso basta escrever
w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

#Saída do modelo
def forward(x):
    return w * x

#Perda
def loss(y, y_pred):
    #A perda é igual ao erro quadrático médio no caso de regressão linear
    #mean() é a média
    return ((y_pred - y)**2).mean()

#Imprimimos a previsão (Saída do modelo) antes do treinamento
#A conta que irá fazer w*x*2 substituindo por números (0.0*0*0) que irá dar 0.000
print(f'Prediction before training: f(5) = {forward(5).item():.3f}')

#Treinamento
#Taxa de aprendizagem
learning_rate = 0.01
#Valor máximo que queremos 
n_iters = 100

for epoch in range(n_iters):
    #A previsão é o passar para a frente
    y_pred = forward(X)
    #Perda
    l = loss(Y, y_pred)
    #Calcular gradientes é o passar para trás
    l.backward()
    #Atualizar os pesos
    #w.data = w.data - learning_rate * w.grad
    with torch.no_grad():
        w -= learning_rate * w.grad
    #zero the gradients after updating
    w.grad.zero_()
    #% -> Corresponte a um mais que será usado no {epoch}
    #O 10 corresponde de quanto em quanto andamos
    #Ou seja irá aparecer epoch 1, epoch 11 ...
    if epoch % 10 == 0:
        #O 1 corresponde ao número onde começa a contagem
        #w -= 0.01 * (np.dot(2*X, (0.0 * X) - Y).mean())
        #loss = (((0.0 * X) - Y)**2).mean()
        #A previsão(w) vai aumentando e a perda(loss) vai diminuindo
        print(f'epoch {epoch+1}: w = {w.item():.3f}, loss = {l.item():.8f}')

#A conta que irá fazer w*x*2 substituindo por números (0.0*5*2) que irá dar 10.000
print(f'Prediction after training: f(5) = {forward(5).item():.3f}')