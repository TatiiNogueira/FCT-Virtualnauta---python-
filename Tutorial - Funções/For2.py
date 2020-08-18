#Função para cada item
fun = [abs(x) for x in [-2, -1, 0, 1, 2]]

#Lista ou tubla
tup = [(y, y**2) for y in range (1, 11)]

#Loop com Loop
Lista1 = []
for a in range (4):
    for b in range (4):
        if a != b:
            Lista1.append([a,b])

#Loop com Loop de uma forma mais simples
Lista2 = [[a, b] for a in range(4) for b in range(4) if a != b]
