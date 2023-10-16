from random import randint ##Importado para el ejercicio 3

###Ejercicio 1

fp = open("texto.txt", "r")
datos = fp.read(10)
print(datos)
datos= fp.read(8)
print(datos)
fp.close() 

### Ejercicio 2
fichero = open("texto.txt", "r")
linea = fichero.readline()  ##Si no lo imprimes no te muestra esa linea
print(linea)                ## pero es necesario ponerlo, ya que el va leyendo linea a linea
linea= fichero.readlines()  ## Retorna una lista
print(linea)
linea= fichero.readline()   ##Retorna una cadena de caracteres
print(linea)
fichero.close()

###Explicacion
lista = ["Nobody is listening\n","Ostia tio\n", "Ajdaiwao\n"]
for palabra in lista:
    palabra.replace("\n","") ## Esto sirve para reemplazar ese caracter, toca hacerlo asi pq los string son inmutables
    print(palabra)

### Ejercicio 3
lista = []

for i in range(50):
        lista.append(randint(0,100))
        maximo = str(max(lista))
        minimo = str(min(lista))
        prom = str(sum(lista)/len(lista))

        file_datos = open("datos.txt","a")
        file_datos.write(maximo)
        file_datos.write("\n")
        file_datos.write(minimo)
        file_datos.write("\n")
        file_datos.write(prom)
        file_datos.write("\n")
        file_datos.write("Siguiente par de datos")
        file_datos.close()
        print("Archivo creado...")

### Creacion de contextos (with)
nombre_archivo = input("Ingrese el nombre del archivo")
nombre_archivo += ".txt"

with open(nombre_archivo, "w") as archivo:
    datos = input("Ingrese los datos que desea escribir en el archivo")
    archivo.write(datos)

with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo")
    print(contenido) 