n = int(input("Regalame un numero: "))
contador = 10
while contador > 0:
    resultados = n*contador
    contador -= 1 
    print(f'{n} X {contador + 1} es igual a: ' , resultados)
