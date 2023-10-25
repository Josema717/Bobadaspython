import csv 

with open("C:\Programacion\Bobadaspython\Ejercicios_textos\datos.csv", "a", newline="") as archivoCSV:
    contenido = csv.writer(archivoCSV, delimiter=",")
    contenido.writerow([input("Regalame tu nombre> "), input("Regalame tu edad> ")])
    
with open("C:\Programacion\Bobadaspython\Ejercicios_textos\datos.csv", "r", newline="") as archivoCSV:
    datos = csv.reader(archivoCSV, delimiter=',')
    for lineas in datos:
        print(", " .join(lineas))
