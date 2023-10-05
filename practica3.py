from random import randint
def menu():
    print("1, Imprimir matriz\n2. Intercambiar\n3. Salir del programa")
    op = int(input("Seleccione una opcion>>> "))
    return op 
def crear_matriz(n):
    columnas = n 
    filas = n 
    matriz = []    
    for i in range(filas): 
        matriz.append([]) 
        for j in range(columnas):
            matriz[i].append(randint(0,100))
    return matriz 
def intercambiar(matriz_nxn):
    for i in range(len(matriz_nxn)):
        for j in range(len(matriz_nxn[0])):
            x = matriz_nxn[i][j]
            if x%2 == 0:
                matriz_nxn[i][j] = "X"
            else:
                matriz_nxn[i][j] = "O"
            return matriz_nxn
def main():
    n = int(input("Ingrese un numero>>> "))
    if n in range(5,11): 
        matriz_nxn = crear_matriz(n) 
        op = menu()
        if op == 1:
            for row in matriz_nxn:
                for elem in row:
                    print(elem, end='\t')
                print()
        elif op == 2:      
            matriz_cambiada = intercambiar(matriz_nxn)
            for row in matriz_cambiada:
                for elem in row:
                    print(elem, end='\t')
                print()
    else:
        print("Por favor ingrese valores entre 5 y 11 :)")
        
if __name__ == "__main__":
    main()