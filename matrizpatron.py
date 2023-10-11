## La funcion debe tomar un valor N, y hacer una matriz tamaño nxn
## Los valores mas externos deben tener 1, la siguiente barrera interior
## debe tener 2, y asi sucesivamente

## Pseudocodigo
## Se debe imprimir una matriz
## 
## 
## 
## 
## 
## 
## 
def matrix(n):
    for i in range(n):
        rango = list(range(n))
        for j in range(n):
            print(min(i, j, n - i-1 , n - j-1 ) + 1, end=" ")
        print()                                           
n = int(input('Ingresa un numero>> '))                    
print(matrix(n))
