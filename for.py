acumulador = 0
n = int(input("Ingrese un número entero positivo: "))
for numero in range(2, n+1, 2):
    acumulador += numero  
print("El resultado de la suma es:", acumulador )
