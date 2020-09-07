
def edad(edadActual, añoActual):
    if edadActual > 0:
        if añoActual > 0:
            años = 2070 - añoActual 
            edadNueva = edadActual + años
            return edadNueva
        else:
            print("El año ingresado es negativo")
    else:
        print("La edad ingresada es negativa")

def numeroPar(numero):
    if (numero % 2) == 0:
        par = True
    else:
        par = False
    if par:
        print("El numeroes par")
    else:
        print("El impar")
    return par

def pala(palabra):
    primerCaracter = palabra[0]
    ultimoCaracter = palabra[len(palabra)-1]
    print(f"El primer caracter es {primerCaracter}")
    print(f"El último caracter es {ultimoCaracter}")
    return primerCaracter, ultimoCaracter