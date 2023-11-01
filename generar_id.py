import csv 
from random import randint, uniform 

def generador_id():
        letra = chr(randint(65,90))
        letra += chr(randint(65,90))
        letra += str(randint(1000, 9999))
        return letra 
def crear_archivo():
    with open("id_generados.csv" , "w", newline="") as archivo:
        filas = csv.writer(archivo)
        encabezados = []
        encabezados.append("Edad")
        encabezados.append("Estatura")
        encabezados.append("Peso")
        encabezados.append("ID")
        filas.writerow(encabezados)
        matriz = [] 
        for i in range(100):
            matriz.append([])
            edad = randint(0,100)
            matriz[i].append(edad)
            estatura = round(uniform(0.5 , 2.2) ,2)
            matriz[i].append(estatura)
            peso = round(uniform(40, 150), 2)
            matriz[i].append(peso)
            id = generador_id()
            matriz[i].append(id)
        filas.writerows(matriz) 
crear_archivo()
print("archivo creado...")
#letra = chr(68)
#print(letra)
