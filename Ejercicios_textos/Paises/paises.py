import csv 
with open('C:\Programacion\Bobadaspython\Ejercicios_textos\Paises\paises.csv' , 'r') as archivo_csv:
    reader = csv.reader(archivo_csv)
    # for row in reader:
    #     for p in range(row):
    #         IDP = int(row[p]//row[p+1])
    #         print(f"El indice de densidad de poblacion de {row[0]} es igual a: ", IDP)
    columna_deseada = [fila[1] for fila in reader]           
    for h in columna_deseada:
        
        print(columna_deseada)