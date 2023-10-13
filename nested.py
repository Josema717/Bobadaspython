##El codigo debe imprimir un diamante que tenga una altura N, N valor ingresado por el usuario
## Pseudo
## FOR i in range(n)
##   PRINT los espacios necesarios, esto va relacionado a la cantidad de * que hay que imprimir
##      PRINT el * dependiendo de la posicion en la piramide
## FOR j in range(N-2), para que empiece a dibujar el diamante por abajo
##    PRINT los espacios necesarios
##    PRINT * dependiendo de la posicion en la piramide
n = int(input('Ingresa un numero>> '))
if n%2 == 0:
    n +=1 
for i in range(1, n+1, 2): ## Rango = [1, 3, 5]
    espacios = (n - i) // 2             
    print(" "* espacios, '*'*i)
for j in range(n-2, 0, -2):      #n = 4+1, Rango = [3, 1]
    espacios = (n - j) // 2
    print(" "* espacios, '*'*j )
## Buena bro, lo hiciste, eres un grande.