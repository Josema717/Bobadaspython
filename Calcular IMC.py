Nombre = input("Hola, como tu te llama: ")
Edad = int(input("Cuantos años tienes: "))
Estatura = float(input("Cuanto mides viejo?, Responde en metros porfa: "))
Peso =int(input("Cuanto pesas?, Responde en Kg por favor:"))

IMC = Peso/Estatura**2

print(f"Esta persona tiene un IMC de: {IMC:0.2f}")
if IMC < 18.5:
    print("Oye mani, estás llevado ey")
else:
    print(f"Ah nombe {Nombre} Estás parado en la raya")
