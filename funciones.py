
def edad(edad_actual, año_actual):
    if edad_actual > 0:
        if año_actual > 0:
            años = 2070 - año_actual 
            edad_futura = edad_actual + años
            return edad_futura
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
        print("Es par")
    else:
        print("Es impar")
    return par

def pala(palabra):
    primer_caracter = palabra[0]
    segundo_caracter = palabra[len(palabra)-1]
    print(f"El primer caracter es {primer_caracter}")
    print(f"El último caracter es {segundo_caracter}")
    return primer_caracter, segundo_caracter