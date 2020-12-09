#Link -> https://www.youtube.com/watch?v=YAJ5XBwlN4o&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=7

#Módulos
import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

#0) Preparar os dados
#Dados de regressão
X_numpy, y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)

#Cast to float Tensor - Elenco para flutuar Tensor
X = torch.from_numpy(X_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))
#Se comentar a linha ou trocar o primeiro y por outra linha o gráfico deseja uma linha reta
#Onde está o 1 se colocar -1 não faz diferença
y = y.view(y.shape[0], 1)
#Indicamos que o número de amostras e númmeros de recursos são X.shape para que possamos usar isto em um segundo
n_samples, n_features = X.shape

#1) Modelo
#Linear model f = wx + b
input_size = n_features
output_size = 1
model = nn.Linear(input_size, output_size)

#2) Perda e Otimicador
learning_rate = 0.01
#Calcula o erro quadrático médio
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  

#3) Loop de treinamento
#Definir o número de épocas
num_epochs = 100

for epoch in range(num_epochs):
    #Passar para a frente
    y_predicted = model(X)
    #Perda para a frente
    loss = criterion(y_predicted, y)
    #Passar para trás
    loss.backward()
    #Update para trás
    optimizer.step()
    #zero_grad antes da nova etapa
    optimizer.zero_grad()
    #% -> Corresponte a um mais que será usado no {epoch}
    #O 10 corresponde de quanto em quanto andamos
    #Ou seja irá aparecer epoch 10, epoch 20...
    if (epoch+1) % 10 == 0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')

#% -> Corresponte a um mais que será usado no {epoch}
    #O 2 corresponde de quanto em quanto andamos
    #Ou seja irá aparecer epoch 1, epoch 3 ...
        #O 1 corresponde ao número onde começa a contagem

#Plot
predicted = model(X).detach().numpy()
#o - Para pontos, b - Azul, r - vermelho
plt.plot(X_numpy, y_numpy, 'ob')
plt.plot(X_numpy, predicted, 'r')
plt.show()