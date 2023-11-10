def contar(lineas):    ###Esta funciona bien
    n_lineas = len(lineas)
    return n_lineas
### El unico que sirve bien :)
def l_word(texto):
    lista = texto.split()
    palabra_mas_larga = lista[0]
    for palabra in lista:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga, 14
### Aca intente que fuera contando la cantidad de caracteres, y cuando llega
### a la palabra con 14 caracteres. "bioinformatica" pues se detiene y la imprime
### Pero las tildes y los caracteres especiales me mataron

def cambiar(palabra_vieja, palabra_nueva):
    with open('Practicas/frases.txt' , "r") as archivo:
        texto = archivo.read()
        contenido = texto.split()
    with open('Practicas/frases.txt', 'w') as archivo_editable:
        for i in range(len(contenido)):
            if palabra_vieja in contenido[i]:
                contenido[i] == palabra_nueva  
        archivo_editable.write('\n'.join(contenido))
### El programa no encuentra la "palabra_vieja"

def main():
    with open('Practicas/frases.txt' , "r+") as archivo:
        lineas = archivo.readlines()
        archivo.seek(0)
        archivo.seek(0)
        texto = archivo.read()
            

        print("Este es el texto que vamos a usar:")
        for i in lineas:
            print(i)
            print("1. Contar cuantas lineas tiene el archivo\n2. Encontrar la palabra más larga del archivo\n3. Reemplazar una palabra por otra en el archivo\n4. Salir del programa")
            op = int(input("Que deseas hacer con el? "))
            if op == 1:
                n_lineas = contar(lineas)
                print(f"El archivo contiene {n_lineas} frases")
            elif op == 2:
                palabra = l_word(texto)
                print(f"La palabra más larga es {palabra[0]} y tiene {palabra[1]} caracteres")

            elif op == 3:
                palabra_vieja = input("Que palabra deseas reemplazar?  ")
                palabra_nueva = input("Dime la palabra que va a ocupar su lugar   ")
                resultado = cambiar(palabra_vieja, palabra_nueva)
                print(resultado)
main() 
