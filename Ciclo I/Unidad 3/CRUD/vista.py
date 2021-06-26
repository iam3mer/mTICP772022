from logica import *

def menu(dbAnimales:dict)->None:
    while True:
        print('-----CRUD-----')
        print('--------------')
        print('-1- Agregar animal')
        print('-2- Actualizar animal')
        print('-3- Mostrar informacion animal')
        print('-4- Eliminar')
        print('-5- Salir')

        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            dbAnimales = crear(dbAnimales)
        elif opcion == '2':
            dbAnimales = actualizar(dbAnimales)
        elif opcion == '3':
            consultar(dbAnimales)
        elif opcion == '4':
            dbAnimales = eliminarAnimal(dbAnimales)
        elif opcion == '5':
            break

# CREAD
def crear(db:dict={})->dict:

    print('Esta a pundo de añadir un animal')

    animal = input('Ingrese el nombre del animal: ')
    
    while True:
        print('Estructura del animal')
        print('-1- Vertebrado')
        print('-2- Invertebrado')

        estructura = input('Ingrese una de los opciones: ')
        
        msj = 'Ingrese la estructura del del animal de los valores presentados: '
        if estructura == '1':
            print(vertebrados)
            tipo = comprobacion(msj, vertebrados, 'str')
            break
        elif estructura == '2':
            print(invertebrados)
            tipo = comprobacion(msj, invertebrados, 'str')
            break

    print(alimentacion)
    msj = 'Ingrese el tipo de alimentacion de los valores presentados: '
    seleccionAlimentacion = comprobacion(msj, alimentacion, 'str')

    msj = 'Ingrese el tipo de reproduccion de los valores presentados: '
    print(reproduccion)
    seleccionReproduccion = comprobacion(msj, reproduccion, 'str')

    if estructura == '1':
        estructuraAnimal = {
                'vertebrado': True,
                'invertebrado': False,
                'tipo': tipo
            }
    else:
        estructuraAnimal = {
                'vertebrado': False,
                'invertebrado': True,
                'tipo': tipo
            }

    animal = {
        'animal': animal,
        'estructura': estructuraAnimal,
        'alimentacion': seleccionAlimentacion,
        'reproduccion': seleccionReproduccion
    }

    llave = len(db) + 1

    db = agregar(llave, animal)

    return db
    

# READ
def consultar(db:dict={})->None:
    
    print('Consulta de un animal.')

    msj = 'Ingrese el nombre del animal: '
    llaveAnimal = comprobarLlave(msj)

    animalConsultado = leer(llaveAnimal)

    if animalConsultado['estructura']['vertebrado'] == True:
        estructura = 'vertebrado'
    else:
        estructura = 'invertebrado'

    print(f'El animal consultado es {animalConsultado["animal"]}')
    print(f'Estrutura: {estructura}, {animalConsultado["estructura"]["tipo"]}')
    print(f'El animal {animalConsultado["animal"]} es {animalConsultado["alimentacion"]}')
    print(f'Modo de reproducción: {animalConsultado["reproduccion"]}')


# UPDATE
def actualizar(db:dict)->dict:

    print('Actualizar un animal.')

    msj = 'Ingrese el nombre del animal: '
    llaveAnimal = comprobarLlave(msj)

    msj = 'Desea modificar el nombre del animal [S/s] Sí [N/n] No '
    if comprobacionSN(msj):
        animal = input('Ingrese el nuevo nombre: ')
        actualizarValor(llaveAnimal, 'animal', animal)

    msj = 'Desea modificar la alimentación del animal? [S/s] Sí [N/n] No '
    if comprobacionSN(msj):
        print(alimentacion)
        msj = 'Ingrese la alimentación: '
        alimentacion = comprobacion(msj, alimentacion, 'str')
        actualizarValor(llaveAnimal, 'alimentacion', alimentacion)

    msj = 'Desea modificar la reproduccion del animal? [S/s] Sí [N/n] No '
    if comprobacionSN(msj):
        print(reproduccion)
        msj = 'Ingrese la reproducción: '
        reproduccion = comprobacion(msj, reproduccion, 'str')
        actualizarValor(llaveAnimal, 'reproduccion', reproduccion)

    return db

# DELETE
def eliminarAnimal(db:dict)->dict:

    print('Eliminar un animal')

    msj = 'Ingrese el nombre del animal: '
    llaveAnimal = comprobarLlave(msj)

    animal = eliminar(llaveAnimal)

    print(f'Se ha eliminado el animal {animal["animal"]}')

    return db


menu(dbAnimales)