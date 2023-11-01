import csv 
from random import randint, uniform 

with open("id_generados.csv" , "w", newline="") as archivo:
    filas = csv.writer(archivo)
    filas[0].append("Edad")
    filas[0].append("Estatura")
    filas[0].append("Peso")
    filas[0].append("ID")
    next(filas)
    matriz = []
    def generador_id():
        letra = chr(randint(0,))
    for i in range(100):
        matriz.append([])
        for j in range(4):
            matriz.append([])
#letra = chr(68)
#print(letra)
