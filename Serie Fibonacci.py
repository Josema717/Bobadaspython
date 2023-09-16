cantidad_numeros = int(input("Ingrese algun numero entero: "))
if cantidad_numeros <= 0:
        print("Por favor ingrese un numero positivo")
elif cantidad_numeros == 0: 
        print("Serie de Fibonacci")
        print(0) 
else: 
    a = 0 
    b = 1
    print("Serie de Fibonacci")
    print(a)
    print(b)
    contador = 2 
    while contador <= (cantidad_numeros-2):
        c = a + b 
        print(c) 
        a = b 
        b = c 
        contador += 1