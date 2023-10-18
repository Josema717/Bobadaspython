import csv
from random import randint 
# nombre_archivo = "personas.txt"

# with open(nombre_archivo, "r") as file:
#     linea = file.readline() 
#     linea1 = linea.replace("\n", "")
#     lista = linea1.split(",")
#     for i in range(len(lista)):
#         lista[i] = int(lista[i])      ##Convierte a enteros los elementos    

# print(f"La persona con ID: {lista[1]} tiene: {lista[0]} años...")    

# nombre_archivo = "personas.csv"
# with open(nombre_archivo, newline="") as file:
#     archivo = csv.reader(file, delimiter=" ", quotechar= "|") 
#     for row in archivo:
#         print(row)
#Dejalo para despues


"""with open("personas.txt", "r") as file:
    for dato in file:
        dato1 = dato.replace("\n", "")
        lista = dato1.split(",")
        for i in range(len(lista)):
            lista[i] = int(lista[i])
        
        print(f"La persona con ID: {lista[1]} tiene: {lista[0]} años...")"""""

##Generar una matriz de 15x4
## Llenar con datos aleatorios entre 1 y 10
##Escribir esa matriz en un archivo de texto


##Creo la matriz de aleatorios
filas = 15
columnas = 4
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        n_aleatorio = randint(0,10)
        matriz[i].append(n_aleatorio)
nombre_archivo = "pruebamatriz.txt"

with open(nombre_archivo, "w") as archivo:
    for filas in matriz:
        for j in filas:
            j = str(j) + "," 
            archivo.write(j)
        archivo.write("\n")
print(matriz)