#archivo = open("C:\Programacion\Bobadaspython\Ejercicios_textos\input.txt", "r")
#frases = archivo.readlines()
#split_frase = frases[0].split()
#print(frases)
#print(len(split_frase))
#print("Esto es a como lista: ", a_list)  ## Descartado

#fp = open("C:/Programacion/Bobadaspython/Ejercicios_textos/texto2.txt", "r+")
#datos = fp.readline()
#print(datos)
#datos = fp.readlines()
#print(datos)
#texto = "Meros temas los dos"
#fp.write(texto)
#fp.close()

datos = open("C:\Programacion\Bobadaspython\Ejercicios_textos\datos_usuario.txt", "a")
print("Hola bienvenido, regalame los siguientes datos por favor")
print()
nombre = str(input("Regalame tu nombre porfa: "))
edad = str(input("Regalame tu edad: "))
carrera = str(input("¿Que estas estudiando?  "))
estatura = str(input("¿Cuanto mides?  "))


datos.write(nombre)
datos.write("\n")
datos.write(edad)
datos.write("\n")
datos.write(carrera)
datos.write("\n")
datos.write(estatura)
datos.write("\n")
datos.close() 
