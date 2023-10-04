from math import factorial
def comprobar_entero(n):
    valido = True 
    if n < 0:
        valido = False 
    else:
        valido = True 
        return valido 
def calculo_factorial(n):
    contador = 1 
    if n == 0 or n == 1:
        return 1
    else: 
        #n_factorial = factorial(n)
        n_factorial = n*n-contador
        contador -= 1
    return n_factorial 


def main():
    print("Hola bienvenido")
    n = int(input("Regalame un numero entero positivo >>> "))
    if comprobar_entero(n) == True:
        n_factorial = calculo_factorial(n)
        print(f"El valor factorial del numero que ingresaste es {n_factorial}")
    else:
        print("El numero debe ser un valor positivo")
    
if __name__ == '__main__':
    main()