#Juego de adivinar un numero
from random import randint 
def menu():
    print("A, Adivinar\nP. Pista\nS. Salir")
    opcion = input("Ingrese una opcion:")
    return opcion.lower()
x = randint(0,100)
intentos = 10
while intentos > 0 and op != "s":
    op = menu()
    if op == "a":
        n = input("Adivina el numero>>")
        if x == n:
            print("Buena, adivinaste")
        else:
            print(f"Cule bobo, te quedan {intentos} intentos")
        intentos -= 1
    elif op == "p":
        if x > n:
            print("Oe, el numero es mayor")

##Arregla esta mkada cuando llegues a la casa