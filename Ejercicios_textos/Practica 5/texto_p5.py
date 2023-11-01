### with open ("frases.txt", "r") as archivo
### def n_lineas(archivo)
### lineas = archivo.readlines()
### n_lineas = lineas.count()
### return n_lineas


### def l_word(archivo):
### palabras = archivo.read()
###

### def reemplazar(archivo):
### palabras = archivo.read()
### palabra_vieja = input("Que palabra deseas reemplazar?")
### palabra_nueva = input("Que palabra quieres que esté ahi?")
### palabras = palabras.replace(palabra_vieja, palabra_nueva)
### return palabras


def contar(lineas):    ###Esta funciona bien
    n_lineas = len(lineas)
    return n_lineas

def l_word(texto):
    lista = texto.split(" ")
    for palabra in lista:
        caracteres = len(palabra)
        if len(palabra) == 20:
            return palabra, 20


def cambiar(palabras, palabra_vieja, palabra_nueva):
    for palabra in palabras:
        palabras.replace(palabra_vieja, palabra_nueva)
    return palabras


