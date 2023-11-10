import csv

def leer_extenso(): 
    with open("paises.csv", "r", newline="") as archivo_csv: 
        leer = csv.reader(archivo_csv)
        mayor_extension = 0  #se le da el valor de cero a esa variable para que se pueda comparar
        next(leer) #comienza en la línea siguiente del archivo 
        for fila in leer: 
            if int(fila[3]) > mayor_extension: #compara el valor de la cuarta columna con el de mayor extensión 
                mayor_extension = int(fila[3])  #se guarda el nuevo valor de mayor extension 
                pais_mayorextension = fila[0] #corresponde a la posición del nombre del país 
                capital_mayorextension = fila[2] #es el numero de posición que le corresponde a la capital 
                habitantes_mayorextension = fila[1] #es el numero de posición que le corresponde a los habitantes
            
        print(f"El país con mayor extensión es: {pais_mayorextension}")
        print(f"Capital: {capital_mayorextension}")
        print (f"Habitantes: {habitantes_mayorextension}")
        print (f"Extensión: {mayor_extension} km²") 

def buscar_pais(nombre):
    
    with open("paises.csv", "r", newline="") as archivo_csv:
        leer = csv.reader(archivo_csv)
        matriz = []#se crea una lista vacía para meter los datos del archivo aahí 
        for fila in leer:  
            matriz.append(fila) #agrega todos los datos del archivo a la lista
                                 # Buscar el país ingresado por el usuario
        pais_encontrado = None #se le da el valor de None a la variable para ser comparado más adelante 
        for pais in matriz: #itera sobre cada elemento de matriz 
            if pais[0].capitalize() == nombre:  # Convertir a mayúscula la primera letra, se va la posición cero de la fila (que es la de los nombre) y mira si el parametro ingresado por el usuario es el mismo que el valor que hay en la fila
                pais_encontrado = pais #se guarda el nombre del país si esta en la lista, en la sigueinte variable
            
        if pais_encontrado: 
            print(f"La información encontrada sobre {pais_encontrado[0]}:") #se imprime el guardado en la posición cero(nombre del país)
            print(f"Capital: {pais_encontrado [2]}") #se imprime el guardado en la posición 2(capital)
            print (f"Habitantes: {pais_encontrado[1]}") # "              "
#· ""                en la posición 38()extensión            setnataibah()13 nóicisop al ne 
            print (f"Extensión: {pais_encontrado [3]} km²") 
        else: 
            print("El país que usted ingresó no se encuentra en la lista")

def leer_poblado(): 
    with open("paises.csv", "r", newline="") as archivo_csv:
        leer = csv.reader(archivo_csv)
        next(leer) #comienza en la línea siguiente del archivo 
        mayor_poblacion = 0 #se le da el valor de cero a esa variable para que se pueda comparar
        for fila in leer: 
            if int(fila[1]) > mayor_poblacion: #compara el valor de la segunda con el de mayor población 
                mayor_poblacion = int(fila[1])  #se guarda el nuevo valor de mayor población 
                pais_mayorpoblacion = fila[0] #corresponde a la posición del nombre del país 
                capital_mayorpoblacion = fila[2] #es el numero de posición que le corresponde a la capital 
                extension_mayorpoblacion = fila[3] #es el numero de posición que le corresponde a los habitantes
            
        print(f"El país con mayor población es: {pais_mayorpoblacion}") #imprime los valores de las variables ya asignadas
        print(f"Capital: {capital_mayorpoblacion}")
        print (f"Habitantes: {mayor_poblacion}")
        print (f"Extensión: {extension_mayorpoblacion} km²") 

                           ### Se pone esta linea para evitar la linea de los enunciados
def letra_inicial(a):                            
    with open("paises.csv" , newline="") as archivo_csv:    
        datos = csv.reader(archivo_csv)                 ### se abre el archivo en modo lectura
        next(datos)         
        paises = []                                 ### Se crea una lista vacia
        for fila in datos:                          ### Se va iterando en cada fila, en la columna de los paises
            pais = fila[0]                          ### Se toma cada pais y se evalua la posicion 0, osea la primera letra        if pais[0] == a:                        ### si esta primera letra es igual a la ingresada por el usuario
            if pais[0] == a:                
                paises.append(pais)                 ### se agrega a la lista
    return paises
    
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

def maximo_idc():                                           
    with open('paises.csv', newline='') as archivo2:  # Se abre el archivo que se creó en la funcion "densidad()"
            datos2 = csv.reader(archivo2)                   
            next(datos2)
            maxima_densidad = 0
            pais_mas_denso = None
            for fila in datos2:                             # Se recorren todas las filas del archivo csv
                pais = fila[0]                              
                habitantes = float(fila[1])                 ## Los habitantes son la columna 2, por esto se toma fila en la posicion 1
                extension = float(fila[3])                  ## Lo mismo con la extension
                densidad = habitantes // extension          ## Se hace el calculo
                if densidad > maxima_densidad:              ## La densidad maxima empieza en 0, se va haciendo la prueba de cada valor de densidad calculado en la linea anteriorer
                    maxima_densidad = densidad              ## Si este valor supera a la densidad anterior, pasa a ser la maxima densidad
                    pais_mas_denso = pais                  
            return pais_mas_denso , maxima_densidad
        
def main(): 
    loop = True
    print("1. Buscar País\n2. Buscar país por letra\n3. Encontrar País más poblado\n4. Encontrar el país más extenso\n5. País más denso \n6. Nuevo archivo \n7. Salir del programa")
    while loop: 
        option = int(input("Ingrese una opción por favor>> "))
        if option == 1:
            nombre_pais = input("Ingrese el nombre del país: ").capitalize()  
            buscar = buscar_pais(nombre_pais) 
            print(buscar)
        elif option == 2:
            letra = input("Ingresa una letra: ")
            lista_paises = letra_inicial(letra)
            print(f'Los paises que inician con la letra {letra} son: ')
            for pais in lista_paises:
                print(pais)
        elif option == 3: 
            leer_poblado()
            
        elif option == 4:
            leer_extenso()
            
        elif option == 5: 
            with open('paises.csv', newline='') as archivo: 
                datos = csv.reader(archivo)
                pais, densidad = maximo_idc()
                next(datos)
                for filas in datos:
                    if filas[0] == pais:
                        print(f'El pais más denso es {filas[0]}, con una poblacion de {filas[1]} habitantes, su capital es {filas[2]}, y tiene una extension de {filas[3]}Km cuadrados')
                        
        elif option == 6:
            densidad()
            print('Archivo creado ...')
 
      
        elif option == 7: 
            loop = False 
            print("Saliendo del programa...")
        else: 
            print("Ingrese una opción válida")
main()   