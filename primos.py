# Escribir un programa que me muestre los numero primos entre 1 y 100

def primos(limite = 0):
    """
    Esta función imprime en pantalla los numeros primos hasta el limite que
    se pase como argumento.

    Si no se pasa el argumento, se solicitara al usuario el ingreso por teclado.
    """
    if limite == 0:
        limite = int(input('Ingrese el limite: '))

    contador = 2
    aux = 1
    primo = 0
    while contador <= limite:
        while aux <= contador:
            if contador % aux == 0:
                primo = primo + 1
            aux = aux + 1
        if primo == 2:
            print(contador)
        contador = contador + 1
        primo = 0
        aux = 1

primos(40)
