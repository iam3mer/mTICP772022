from datos import *

# CREATE
def agregar(llave:int, valor:dict)->dict:
    dbAnimales[llave] = valor

# READ
def leer(llave:int)->dict:
    return dbAnimales[llave]

# UPDATE
def actulizar(llave:int, valor:dict)->dict:
    dbAnimales[llave] = valor

# DELETE
def elmiminar(llave:int)->dict:
    return dbAnimales.pop(llave)

# Funciones de comprobación
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