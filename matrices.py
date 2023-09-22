from random import randint

filas = 4 
columnas = 10
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        aleatorio = randint(100,500)
        matriz[j].append(aleatorio)

print(matriz)
