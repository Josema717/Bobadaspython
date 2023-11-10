import csv 

def autenticar_usuario(cuenta, password):
    with open("Ejercicios_textos\Banco maicao\cuentas.csv", newline="") as cuentas_csv:
        datos = csv.reader(cuentas_csv)
        next(datos)
        for filas in datos:
            if int(filas[0]) == int(cuenta) and filas[1] == password:
                return True
            return False 
def consultar_saldo(cuenta):
    with open("Ejercicios_textos\Banco maicao\cuentas.csv", newline="") as cuentas_csv:
        datos = csv.reader(cuentas_csv)
        lista = []
        for fila in datos:
            lista.append(fila)
        cuenta_encontrada = None 
        for cuenta in lista:
            if lista[0] == cuenta:
                cuenta_encontrada = cuenta
            if cuenta_encontrada:
                saldo = lista[2][2]
                return saldo 
def consignacion(cuenta_2, valor):
    with open("Ejercicios_textos\Banco maicao\cuentas.csv", newline="") as cuentas_csv:
        reader = csv.reader(cuentas_csv)
        matriz = []
        for filas in reader:
            matriz.append(filas)
        for i in range(1, len(matriz)-1):
            if matriz[i][0] == cuenta_2:
                saldo = matriz[i][2]
                saldo += valor
                print("consignacion exitosa")
            else:
                print("No se encontro el numero de cuenta a consignar")
    with open("Ejercicios_textos\Banco maicao\cuentas.csv", "w", newline="") as archivo_editable:
        writer = csv.writer(archivo_editable)
        writer.writerows(matriz)

def realizar_retiro(cuenta, valor):
    with open("Ejercicios_textos\Banco maicao\cuentas.csv", newline="") as cuentas_csv:
        datos = csv.reader(cuentas_csv)
        matriz = []
        for filas in datos:
            matriz.append(filas)    
        for i in range(1, len(matriz)-1):
            saldo_actual = matriz[i][2]
            if matriz[i][0] == cuenta and saldo_actual >= valor:
                saldo_actual -= valor
                print("Retiro exitoso")
            else:
                print("No se encontro la cuenta, o no tienes fondos suficientes")
        with open("Ejercicios_textos\Banco maicao\cuentas.csv", "w", newline="") as archivo_editable:
            writer = csv.writer(archivo_editable)
            writer.writerows(matriz)
def main():
    print("Bienvenido al banco de Maicao")
    print("1. Autenticar usuario \n2. Consultar saldo \n3. Realizar consignacion \n4. Realizar retiro")
    op = int(input("¿Que deseas hacer?" ))
    cuenta = input("Ingresa tu numero de cuenta: ")
    password = input("Ingresa tu contraseña: ")
    if op == 1:
        verificado = autenticar_usuario(cuenta, password)
        if verificado:
            print("Verificacion exitosa")
        else:
            print("Por favor ingresa los datos nuevamente")
    elif op == 2:
        saldo = consultar_saldo(cuenta) 
        print(f"Tu saldo actual es de {saldo} pesos")
    elif op == 3:
        cuenta_recibe = input("Ingrese la cuenta que recibira la consignacion")
        cantidad = int(input("Ingrese el valor que desea consignar"))
        consignacion(cuenta_recibe, cantidad)
    ## No voy a continuar el main pq no hace falta
main()

