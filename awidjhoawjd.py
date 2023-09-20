#Ejercicio 7
print(45*"-")
print("Grador Celcius\t\tGrados Fahrenheit")
print(45*"-")
for temp in range(0,101,10):
    print(f"{temp}\t|\t{(temp*9/5)+32}")
