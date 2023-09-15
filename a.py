envio = 0
compra = int(input("Ingresa el valor de la compra:  "))
if compra < 100000:
    envio = 9000
total = envio + compra
print(f"El total de su compra con envio es de:{total}")
