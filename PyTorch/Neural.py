#Rede Neural multicamada que pode fazer a classificação de digitos
#Link -> https://www.youtube.com/watch?v=oPhxf2fXHkQ&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=13

#Módulos
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

#Configuração do dispositivo
#Se cuda for aceite pelo sistema esse será o nome do dispositivo se não o nome será cpu
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#Hiperparametros
#Tamanho de entrada, as imagens irão ter de tamanho 28x28, por isso o input_size é 784 porque 28*28 = 784
input_size = 784 
#Tamanho oculto
hidden_size = 500
#Número de classes, aqui tem de ser 10, porque temos 10 classes diferentes
num_classes = 10
#Número de épocas, temos 2 digidos de 0 a 9
num_epochs = 2
#Tamanho do lote
batch_size = 100
#Taxa de aprendizagem
learning_rate = 0.001

#Conjunto de dados MNIST
train_dataset = torchvision.datasets.MNIST(root='./data',train=True,transform=transforms.ToTensor(),download=True)
test_dataset = torchvision.datasets.MNIST(root='./data',train=False,transform=transforms.ToTensor())

#Carregador de dados
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size,shuffle=False)

#Conversão para objeto erro
examples = iter(test_loader)
example_data, example_targets = examples.next()

#6 - É o número de quadrados que queremos
for i in range(6):
    #Indicamos que queremos 2 linhas, 3 colunas
    plt.subplot(2,3,i+1)
    plt.imshow(example_data[i][0], cmap='gray')
plt.show()

#Rede neural totalmente conectada com uma camada oculta
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.input_size = input_size
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, num_classes)  
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        #Sem ativação e sem softmax no final
        return out

model = NeuralNet(input_size, hidden_size, num_classes).to(device)

#Perda
criterion = nn.CrossEntropyLoss()
#Otimizador
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)  

#Treine o modelo
n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):  
        #Forma de origem: [100, 1, 28, 28]
        #Redimensionado: [100, 784]
        images = images.reshape(-1, 28*28).to(device)
        labels = labels.to(device)
        #Passar para a frente
        outputs = model(images)
        loss = criterion(outputs, labels)
        #Retroceder e otimizar
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print (f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{n_total_steps}], Loss: {loss.item():.4f}')

#Teste o modelo
#Na fase de teste, não precisamos calcular gradientes (para eficiência de memória)
with torch.no_grad():
    #Número de previsões
    n_correct = 0
    #Número de amostras
    n_samples = 0
    for images, labels in test_loader:
        images = images.reshape(-1, 28*28).to(device)
        labels = labels.to(device)
        outputs = model(images)
        #Retornos máximos (valor, índice)
        _, predicted = torch.max(outputs.data, 1)
        n_samples += labels.size(0)
        n_correct += (predicted == labels).sum().item()

    acc = 100.0 * n_correct / n_samples
    print(f'Accuracy of the network on the 10000 test images: {acc} %')