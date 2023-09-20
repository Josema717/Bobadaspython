#Ejercicio 6 de bucles
contador = 0
acumulador = 0 
n = float(input("Ingresa tus notas, una vez termines agrega un 0 como ultimo valor>>"))
while n > 0:
    acumulador += n 
    contador += 1
    n = float(input("Ingresa tus notas, una vez termines agrega un 0 como ultimo valor>>"))
resultado = acumulador/contador 
print(f"Tu promedio es de {resultado:0.2f}")
