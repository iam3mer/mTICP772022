# Funcionar Saludar
def saludar()->str:
    return f'Hola Tripulantes!'

saludar()
saludar()
saludar()
saludar()
saludar()
#print()

for i in range(5):
    saludar()

# Funcion de orden superior
def nVeces(otraFuncion, n):
    for _ in range(n):
        print(otraFuncion())
#print()

#nVeces(saludar, 10)

def despedirse():
    print('Adios!')

#nVeces(saludar,5)
#nVeces(despedirse,5)

# Funciónes Lambda
def moneda(pesos:float)->float:
    conversion = round(pesos / 3715, 2)
    return conversion

def moneda(pesos:float)->float:
    return round(pesos / 3715, 2)

def moneda(pesos:float)->float: return round(pesos / 3715, 2)
#print(moneda(5000000))

conversion = lambda pesos: round(pesos / 3715, 2)
# print(tuple(conversion)) # No se puede

conversion = lambda pesos, dolar: pesos / dolar
#print(conversion(2000000, 3715))

# impar
def impar(num)->bool:
    if num%2 != 0:
        return True

impar = lambda num: num%2 != 0
#print(impar(5))

# sciling
cadena = 'Hola Tripulantes'
#print(cadena[::-1])

revertir = lambda cadena: cadena[::-1]
#print(revertir(cadena))

# Operador MAP
def add_5(num):
    return num + 5

# map(funcion, secuencia)
numeros = [2345,45,4576,568,5687,45,53,45323,46467,5678,678,45,23,45]
numeros5 = []
for num in numeros:
    numeros5.append(add_5(num))
#print(numeros5)

#print(list(map(add_5, numeros)))

resultado = list(map(lambda num: num + 5, numeros))
#print(resultado)

impares = list(map(lambda num: num%2 != 0, numeros))
#rint(impares)

# Operador FILTER
# Obtener los numeros impares de una lista
def obtenerImpares(secuencia:list)->list:
    impares = []
    for i in secuencia:
        if impar(i):
            impares.append(i)
    return impares

#print(obtenerImpares(numeros))

impares = list(filter(impar, numeros))
impares = list(filter(lambda num: num%2 != 0, numeros))
#print(impares)

resultado = list(filter(lambda num: num + 5, numeros))
print(resultado)

# Operador REDUCE
from functools import reduce

def promedio(secuencia:list)->float:
    cantidadElementos = len(secuencia)
    acumulador = 0
    for num in secuencia:
        #acumulador = acumulador + num
        acumulador += num
    resultado = acumulador / cantidadElementos
    return round(resultado,2)

#print(promedio(numeros))

promedio = reduce(lambda x, y: x + y, numeros) / len(numeros)
#print(round(promedio, 2))

# ZIP

letras = ['a','b','c','d','e','f','g']
numeros2 = [5476,435,567,457,678,89,465]

numeros = zip(letras, numeros2)
print(list(numeros))