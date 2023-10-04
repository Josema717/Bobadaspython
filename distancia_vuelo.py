x_coords = []
y_coords = []
def verifica_vectores(x_coords, y_coords):

    vectores_correctos = True 

    a = len(x_coords)
    b = len(y_coords)
    if a != b:
        vectores_correctos = False   
    else:
        vectores_correctos = True 
    return vectores_correctos

def distancia_entre_puntos(x_coords, y_coords):
    from math import sqrt
    for i in range(0, len(x_coords)-1): 
        x = x_coords [i]
        p = x_coords [i+1]
        y = y_coords [i] 
        n = y_coords [i+1]
        
               #Como saco los valores de el for, para poder trabajar con ellos
        d = 2*sqrt((p-x)**2+(n-y)**2)
    return d 
def main():
    contador = int(input("¿Cuántas coordenadas quiere ingresar?")) #El contador es la cantidad de coords
    acumulador = 0       #Solo lo hago para que tenga algo de orden para el print
    while contador > 0 and acumulador != contador:
        x = int(input(f"Ingrese coordenada en x{acumulador + 1}>>  "))      #Para que vaya indicando el subindice de x
        y = int(input(f"Ingrese coordenada en y{acumulador + 1}>>  "))      # O el subindice de Y
        contador -= 1 
        acumulador += 1 
        x_coords.append(x)
        y_coords.append(y) 

    if verifica_vectores(x_coords, y_coords) != True:
        print("Los vectores tienen longitudes diferentes")
    else: 
        d = distancia_entre_puntos(x_coords, y_coords)
        print(f"La distancia total recorrida es: {d}")
        print("Gracias por utilizar el programa. ¡Hasta luego!")
if __name__ == "__main__":
    main()