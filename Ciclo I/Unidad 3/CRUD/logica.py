from datos import *

# CREATE
def agregar(llaveAnimal:int, infoAnimal:dict)->dict:
    dbAnimales[llaveAnimal] = infoAnimal
    return dbAnimales

# READ
def leer(llaveAnimal:int)->dict:
    return dbAnimales[llaveAnimal]

# UPDATE
def actualizarValor(llaveAnimal:int, llaveSec, infoAnimal:dict)->dict:
    dbAnimales[llaveAnimal][llaveSec] = infoAnimal

# DELETE
def eliminar(llaveAnimal:int)->dict:
    return dbAnimales.pop(llaveAnimal)

# Funciones de comprobación

def comprobarLlave(msj:str)->int:
    keys = list(dbAnimales.keys())
    listaAnimales = []
    for key in keys:
        animal = leer(key)
        listaAnimales.append(animal['animal'])

    print(listaAnimales)
    llaveAnimal = comprobacion(msj, listaAnimales, 'str')

    for key in keys:
        animal = leer(key)
        if llaveAnimal == animal['animal']:
            return key

def comprobacion(msj:str, lista:list, tipo:str)->str:
    while True:
        if tipo == 'int':
            entra = input(msj)
            if entra.isdigit():
                entra = int(entra)
        elif tipo == 'str':
            entra = input(msj)

        for item in lista:
            if entra == item:
                return entra

def comprobacionSN(msj:str):
    while True:
        entrada = input(msj)
        if entrada in ['S', 's', 'si', 'SI']:
            return True
        elif entrada in ['N', 'n', 'no', 'NO']:
            return False