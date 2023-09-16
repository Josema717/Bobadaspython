numeros_pares = []
n = int(input("Regalame un numero: "))
contador = n
lim= n*2 
for numero in range(2, lim+1, 2):
    contador -= 1
    numeros_pares.append(numero)
print(f"Los primeros {n} numeros pares son: " ,numeros_pares)

