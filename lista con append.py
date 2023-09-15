numeros_pares = []
n = int(input("Regalame un numero: "))
contador = n 
for numero in range(2, n+1, 2):
    contador -= 1
    numeros_pares = numeros_pares.append(numero)
print(numeros_pares)

