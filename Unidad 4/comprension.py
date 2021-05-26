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
print(tablas)

