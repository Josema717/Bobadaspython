###Voy a hacer una funcion que valore si el numero entregado es primo o no
### Ademas otra funcion que te entregue los numeros primos en un rango
#entregado por el ususario

##Pseudocodigo
## Pedir al usuario un valor N
## Pasa la FUNCION determinar_primo
## Crear PRIMO = True
## LISTA = [2,3,5,7]
## FOR p in LISTA:
##    IF n%p == 0:
##         PRIMO = True
##    else:
##         PRIMO = False
## IF Primo
##      return True


def determinar_primo(n):
    #primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,97]
    primo = True 
    if n <= 1:
        primo = False
    if n == 2:
        primo = True  
    for p in range(2, int(n**0.5)+1):
        if n%p == 0:
            primo = False
        else:
            primo = True 
    return primo 
def primos_rango(a,b): 
## Recibir el rango del usuario, comprobar cual valor es mayor y que este encabece el rango
## lista_primos = []
## IF a > b: 
###     rango = range(b,a)
## ELIF a < b:
##      rango = range(a,b)
## ElSE:
    ## return ValueError 
## FOR n in range(a,b)
##      FOR d in range(2, int(n**0.5)+1)
##          IF n%d == 0:
            ##  primo = True
##         ELSE:
##              primo = False
##      IF PRIMO
##          lista_primos.append(n)
##  return lista_primos
    lista_primos = []
    if a > b: 
        rango = range(b,a) 
    elif b > a:
        rango = range(a,b)
    else:
        return ValueError 
    
    for n in rango:
        primo = True 
        for d in range(2, int(n**0.5)+1):
            if n%d == 0:
                primo = False
                break 
        if primo:
            lista_primos.append(n)
    return lista_primos 
def main():
    print("Hola, bienvenido")
    n = int(input("Comprobemos si tu numero es primo>> "))
    primo = determinar_primo(n)
    if primo == False:
        print("Ese numero no es primo")
    else:
        print("Ese numero si es primo, que pro")
    
    
    print("Ahora veremos los numeros primos entre un rango")
    num1 = int(input("Regalame un numero>> "))
    num2 = int(input("Regalame otro numero>> "))
    lista_primos = primos_rango(num1, num2)
    
    if primos_rango(num1,num2) == ValueError:
        print("Los numeros no pueden ser iguales")
    print(f"Los numeros primos en ese rango son: {lista_primos}") 
main() 