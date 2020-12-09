#Descida gradiente com autógrado e retropropagação - Utilizando a biblioteca numpy
#Link -> https://www.youtube.com/watch?v=E-I2DNVzQLg&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=5

#NOTAS:
#Nos prints quando aparece :.nf - O numero que estiver onde está o n é o número de casas decimais
#O x é diferente de X que é uma matriz(array)
#O y é diferente de Y que é uma matriz(array)

#Módulos
import numpy as np

#Regressão linear
#Função que faz a combinação de alguns pesos e nossas entradas
#f = w * x
#Exemplo
#f = 2 * x

#O x/y vai ser igual a uma matriz(array) de pontos numpy(np)
#O dtype é o tipo de dados da matriz(array)
X = np.array([1, 2, 3, 4], dtype=np.float32)
#Como a nosso formula é 2x(f = 2 * x) a matriz de y tem de ser os valores da matriz de x vezes 2
Y = np.array([2, 4, 6, 8], dtype=np.float32)

#Inicializamos, para isso basta escrever
w = 0.0

#Saída do modelo
def forward(x):
    return w * x

#Perda
def loss(y, y_pred):
    #A perda é igual ao erro quadrático médio no caso de regressão linear
    #mean() é a média
    return ((y_pred - y)**2).mean()

#1/N porque é a média
#J = 1/N * (w*x - y)**2
#dJ/dw = 1/N * 2x(w*x - y)
def gradient(x, y, y_pred):
    return np.dot(2*x, y_pred - y).mean()

#Imprimimos a previsão (Saída do modelo) antes do treinamento
#A conta que irá fazer w*x*2 substituindo por números (0.0*0*0) que irá dar 0.000
print(f'Prediction before training: f(5) = {forward(5):.3f}')

#Treinamento
#Taxa de aprendizagem
learning_rate = 0.01
#Valor máximo que queremos 
n_iters = 20

for epoch in range(n_iters):
    #A previsão é o passar para a frente
    y_pred = forward(X)
    #Perda
    l = loss(Y, y_pred)
    #Gradientes
    dw = gradient(X, Y, y_pred)
    #Atualizar os pesos
    w -= learning_rate * dw
    #% -> Corresponte a um mais que será usado no {epoch}
    #O 2 corresponde de quanto em quanto andamos
    #Ou seja irá aparecer epoch 1, epoch 3 ...
    if epoch % 2 == 0:
        #O 1 corresponde ao número onde começa a contagem
        #w -= 0.01 * (np.dot(2*X, (0.0 * X) - Y).mean())
        #loss = (((0.0 * X) - Y)**2).mean()
        #A previsão(w) vai aumentando e a perda(loss) vai diminuindo
        print(f'epoch {epoch+1}: w = {w:.3f}, loss = {l:.8f}')

#A conta que irá fazer w*x*2 substituindo por números (0.0*5*2) que irá dar 10.000
print(f'Prediction after training: f(5) = {forward(5):.3f}')