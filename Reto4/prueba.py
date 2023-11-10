import csv

def densidad():
    with open("paises.csv" , newline="") as archivo_csv:    
        datos = csv.reader(archivo_csv)
        filas = [fila for fila in datos]                # Se copian todos los datos del archivo en una nueva lista llamda filas
    filas[0].append('Densidad')                         # A esta lista se le agrega el encabezado "Densidad"
    for fila in filas[1:]:                              # Se empieza a iterar, desde la primera posicion, osea sin los encabezados
        habitantes = float(fila[1])                 
        extension = float(fila[3])
        densidad = habitantes // extension
        fila.append(str(densidad))                      # Se agrega los resultados de la densidad a la lista
    with open('paises_n.csv', 'w', newline='') as archivo_editable:     ## Se crea un nuevo archivo, el cual va a contener los valores de densidad
        contenido = csv.writer(archivo_editable)        
        contenido.writerows(filas) 
    pass

def main():
    if 0 == 0:
        densidad()
        print('Archivo creado...')
main()

def leer_poblado(): 
    with open("paises.csv", "r", newline="") as archivo_csv:
        leer = csv.reader(archivo_csv)
        next(leer)
        mayor_poblacion = 0
        for fila in leer: 
            if int(fila[1]) > mayor_poblacion:
                mayor_poblacion = int(fila[1])  
            print(mayor_poblacion)




def leer_extenso(): 
    with open("paises.csv", "r", newline="") as archivo_csv:
        leer = csv.reader(archivo_csv)
        mayor_extension = 0
        next(leer)
        for fila in leer: 
            if int(fila[3]) > mayor_extension:
                mayor_extension = int(fila[3])  
                pais_mayorextension = fila[0]
                capital_mayorextension = fila[2]
                habitantes_mayorextension = fila[1]
            
        print(f"El país con extensión es: {pais_mayorextension}")
        print(f"Capital: {capital_mayorextension}")
        print (f"Habitantes: {habitantes_mayorextension}")
        print (f"Extensión: {mayor_extension} km²") 
