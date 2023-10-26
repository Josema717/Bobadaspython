from random import randint
from math import sqrt
try:
    lista = []
    for i in range(10):
        lista.append(randint(0,10))
    valor = int(input("Ingrese un valor entero: "))
    division = 2//valor
    n_lista = lista[valor]
    if valor > 4:
        print(n)
    if valor == 2:
        print(range())
    if valor == 1:
        import venezuela
except TypeError:
    print("Hay un rango vacio")
except NameError:
    print("Hay una variable que no existe")
except ValueError:
  print("Estas ingresando un valor incorrecto >:(")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except IndexError:
    print("Te estas saliendo de la lista")
except ModuleNotFoundError:
    print("Estas importando un modulo que no tienes")
except:
    print("Ya no se que hiciste")
else:
    print(valor), print(n_lista)
finally:
    print("Ahi vamos como dice Cerati")
