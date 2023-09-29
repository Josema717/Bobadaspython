#Juego de adivinar un numero
from random import randint 
def menu():
    print("A, Adivinar\nP. Pista\nS. Salir")
    opcion = input("Ingrese una opcion:")
    return opcion.lower()
x = randint(0,100)
intentos = 10  
op = menu()
while intentos > 0 and op != "s":
    if op == "a":
        n = int(input("Adivina el numero>>"))
        if x == n:
            print(f"Buena, adivinaste, solo te tomó {intentos} intentos")
        elif n > 100:
            print(f"Mano el numero es maximo hasta 100, te quedan {intentos -1} intentos")
        else:
            print(f"Cule bobo, te quedan {intentos -1} intentos")
        intentos -= 1
    elif op == "p":
        if x > n:
            print("Oe, el numero es mayor")
if intentos == 0: 
    print(f"Mejor suerte la proxima, el numero era {x}")
elif intentos == 5: 
    
##Arregla esta mkada cuando llegues a la casa