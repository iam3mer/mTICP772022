from pprint import pprint as pp
from random import randint, randrange, random, uniform

# Estructuras por extensión

numeros = [5,5,8,5,4,8,5,56,8,6]
estaturas = {'Juan': 170, 'Maria': 165, 'Jhonatan': 176}

# Estruturas por comprension
# listaComprension = [definicionElementoAgregar for variable in otraLista]
listaComprension = []
for num in [1,2,3,4,5,6,7,8,9]: # range(1,10)
    listaComprension.append(num*3)
#print(listaComprension)

listaComprension = [num*3 for num in [1,2,3,4,5,6,7,8,9]]
#print(listaComprension)

# Calcular el radio de un circulo dado su diametro.
# Como entrada se tiene una lista de diametros y
# se desea tener una lista con el respectivo radio
# radio = diametro / 2
diametros = [2,4,6,8,10,12,14,16]
radios = []
def radiosLista(listaDiametros:list)->list:
    for dia in diametros:
        radio = dia / 2
        radios.append(radio)
    return radios
#print(radiosLista(diametros))

radios = [dia/2 for dia in diametros]
#print(radios)

# Calcular el area de un rombo
# area = (d1 * d2) /2
d1 = [2,3,4,5,6,7,8,9]
d2 = [3,4,5,6,7,8,9,10]
def areaRomboLista(d1:list, d2:list)->list:
    areas = []
    for i in range(len(d1)):
        area = d1[i] * d2[i] / 2
        areas.append(area)
    return areas
#print(areaRomboLista(d1,d2))

areas = [d1[i] * d2[i] / 2 for i in range(len(d1))]
#print(areas)

# numeros pares divisibles por 3, desde 0 hasta 100
def pares3(limite:int)->list:
    listPares3 = []
    for num in range(limite+1):
        if num % 2 == 0:
            if num % 3 == 0:
                listPares3.append(num)
    return listPares3
#print(pares3(100))

listPares3 = [num for num in range(101) if num % 2 == 0 if num % 3 == 0]
#print(listPares3)

listPares3 = [num for num in range(101) if num % 6 == 0]
#print(listPares3)

# Obtener los elementos en comun de dos listas
animalesA = ['gato', 'perro', 'pato', 'conejo', 'araña', 'tortuga', 'lobo']
animalesB = ['elefante', 'salamandra', 'conejo', 'lobo', 'bufalo', 'hormiga', 'buho']
comunes = []
def comunesLista(listaA:list, listaB:list)->list:
    comunes = []
    for animalA in listaA:
        for animalB in listaB:
            if animalA == animalB:
                comunes.append(animalA)
    return comunes
#print(comunesLista(animalesA, animalesB))

comunes = [animalA for animalA in animalesA for animalB in animalesB if animalA == animalB]
#print(comunes)

def comunesLista(listaA:list, listaB:list)->list:
    comunes = []
    for animalA in listaA:
        if animalA in listaB:
            comunes.append(animalA)
    return comunes
#print(comunesLista(animalesA, animalesB))

comunes = [animalA for animalA in animalesA if animalA in animalesB]
#print(comunes)

# Construir una funcion que retorne una lista con las llaves de un diccionario
# No se puede usar keys()
estaturas = {'Juan': 170, 'Maria': 165, 'Jhonatan': 176}
def misLlaves(diccionario:dict)->list:
    llaves = []
    for key in diccionario:
        llaves.append(key)
    return llaves
#print(misLlaves(estaturas))

llaves = [key for key in estaturas]
#print(llaves)

# Tablas de Multiplicar
# tablas = {'Tabla del 2': [2,4,6,8,10,12,14,16,18,20], 'Tabla del 3': [....]}
def tablas1_10(limite:int)->dict:
    tablas = {}
    for t in range(2,limite+1):
        auxLista = []
        for n in range(1,11):
            multiplicacion = t * n
            auxLista.append(multiplicacion)
        tablas[f'Tabla del {t}'] = auxLista
    return tablas
#print(tablas1_10(5))

tablas = {f'Tabla del {t}': [t*n for n in range(1,11)] for t in range(2,6)}
#print(tablas)

'''
# Generar numeros aleatorios
# Genera un numero entero de forma aleatoria entre un valor de inicio y un valor final
for num in range(10):
    print(randint(-10,100), end=' ')
print()

# Genera un numero entero de forma aleatoria entre un valor de inicio y un valor final 
# Como parametro opcional, recibe un valor entero de separador
for num in range(10):
    print(randrange(-10,100,25), end=' ')
print()

# Genera un numero flotante entre 0 y 1 (no se toma)
for num in range(10):
    print(random(), end=' ')
print()

for num in range(10):
    print(uniform(-10,100), end=' ')
'''

# {('a','b):345, ('a','c'):485, ...}
listaCiudades = ['a','b','c','d','e'] # [('a','b'), ('a','c'), ('a','d'), ('a','e'), ('b','a'), ...]

# Generar todos los arcos a excepción de los "iguales", ejemplo ('a','a') ('c','c')
'''
arcos = {}
for i in listaCiudades:
    auxCiudades = []
    for j in listaCiudades:
        if i != j:
            auxCiudades.append((i,j))
    arcos[i] = auxCiudades

print(arcos)
'''

arcos = {i: [(i, j) for j in listaCiudades  if i != j] for i in listaCiudades}
#pp(arcos) ## pp: PrettyPrinter, Dar formato a la salida

# Obtener una lista con todos los arcos por ciudades
arcos = list(arcos.values())
pp(arcos)

# Obtener solo los arcos "unicos"
auxArcos = []
i = 0
def funArcos(i,auxArcos):
    for fila in arcos:
        aux = fila[i:len(fila)]
        if aux != []:
            auxArcos.append(aux)
        i += 1
    return auxArcos
#print(funArcos(i,auxArcos))

arcos = funArcos(i,auxArcos)

# Generar una lista con todos los arcos
auxArcos = []
for lista in arcos:
    for par in lista:
        auxArcos.append(par)

auxArcos = [par for lista in arcos for par in lista]
#print(auxArcos)
#print(len(auxArcos))

# Generar las distancias necesarias
numDistancias = len(auxArcos)
distancias = []
for i in range(numDistancias):
    distancias.append(randrange(50,900,30))
#print(distancias)

# Añadir distancias a los arcos
arcos = {}
i = 0
for arco in auxArcos:
    arcos[arco] = distancias[i]
    i += 1
#print(arcos)

# Generar los arcos "dobles"
auxArcos = {}
for arco in arcos:
    auxArcos[(arco[1],arco[0])] = arcos[arco]
#print(auxArcos)

# Diccionario con arcos final
arcos.update(auxArcos)
print(arcos)