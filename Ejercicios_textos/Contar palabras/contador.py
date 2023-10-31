###El programa debe contar cuantas veces se repite una palabra en un archivo de texto
#### with open('palabras.txt', 'r') as archivo
### 
with open('Ejercicios_textos\Contar palabras\palabras.txt' , 'r') as archivo:
    contenido = archivo.read()
### Necesito saber que palabras tiene el archivo
### Sabiendo eso, ya puedo empezar a ver si esa palabra se repite y meter eso a un contador
    palabras = contenido.split(' ')
    frecuencia = 0
    for i in range(len(palabras)):
        if palabras[:i] == palabras[i-1]:
            frecuencia += 1
        print(frecuencia)
        