def contar(lineas):    ###Esta funciona bien
    n_lineas = len(lineas)
    return n_lineas
### El unico que sirve bien :)
def l_word(texto):
    texto.replace("ó", "o")
    texto.replace("é", "e")
    texto.replace("í", "i")
    texto.replace("á", "a")
    lista = texto.split(" ")
    for palabra in lista:
        n_caracteres = len(palabra)
        if n_caracteres == 14:
            return palabra, 14
### Aca intente que fuera contando la cantidad de caracteres, y cuando llega
### a la palabra con 14 caracteres. "bioinformatica" pues se detiene y la imprime
### Pero las tildes y los caracteres especiales me mataron

def cambiar(texto, palabra_vieja, palabra_nueva):
    for palabras in texto:
        palabras.replace(palabra_vieja, palabra_nueva)
    return texto
### El programa no encuentra la "palabra_vieja"


def main():
    with open("C:\\Users\\B09S202est\\Documents\\Jose Almenarez\\Phyton\\Bobadaspython\\Ejercicios_textos\\Practica 5\\frases.txt" , "r+") as archivo:
        lineas = archivo.readlines()
        archivo.seek(0)
        palabras = archivo.readline()
        archivo.seek(0)
        texto = archivo.read()
            

        print("Este es el texto que vamos a usar:")
        for i in lineas:
            print(i)
        op = print("1. Contar cuantas lineas tiene el archivo\n2. Encontrar la palabra más larga del archivo\n3. Reemplazar una palabra por otra en el archivo\n4. Salir del programa")
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
            resultado = cambiar(palabras, palabra_vieja, palabra_nueva)
            print(resultado)
main() 
