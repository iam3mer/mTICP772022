# Ejercicio 1
cadena = 'Hola Tripulantes del Grupo 77'
def longitudPalabras(secuencia):
    return list(map(lambda p: len(p), secuencia.split(' ')))
print(longitudPalabras(cadena))

# Ejercio 2
from functools import reduce
numeros = [1,2,3]
def numero(secuencia):
    return reduce(lambda x, y: str(x) + str(y), secuencia)
print(numero(numeros))

# Ejercicio 3
cadena = ['caballo', 'teatro', 'casa', 'piscina', 'dibujo', 'carro']
def palabras(caracter, secuencia):
    return list(filter(lambda palabra: palabra[0] == caracter, secuencia))
print(palabras('c', cadena))

# Ejercicio 4
cadena1 = 'almendruco'
cadena2 = 'sempiterno'

def rara(secuencia1, secuencia2, separador):
    return list(map(lambda x : x[0] + separador + x[1], zip(secuencia1, secuencia2)))

print(rara([i for i in cadena1], [i for i in cadena2], '-'))