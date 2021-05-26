from logica import *

def menu():
    while True:
        print('-----CRUD-----')
        print('--------------')
        print('-1- Agregar animal')
        print('-2- Actualizad animal')
        print('-3- Mostrar informacion animal')
        print('-4- Eliminar')
        print('-5- Salir')

        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            crear(dbAnimales)
        elif opcion == '2':
            crear(dbAnimales)
        elif opcion == '3':
            crear(dbAnimales)
        elif opcion == '4':
            crear(dbAnimales)

# CREAD
def crear(db:dict={})->dict:

    vertebrados = ['mamifero', 'ave', 'pez', 'reptil', 'anfibio']
    invertebrados = ['porifero', 'cnidario', 'molusco', 'anelido', 'artropodo']
    alimentacion = ['herbivoro', 'carnivoro', 'omnivoro']
    reproduccion = ['oviparo', 'viviparo', 'ovoviviparo']

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

    agregar(llave, animal)

    return db


# READ
def consultar(db:dict={})->None:

    keys = list(db.keys())

    print('Consulta de un animal x')
    msj = 'Ingrese un numero entero: '
    llaveAnimal = comprobacion(msj, keys, 'int')

    animalConsultado = db[llaveAnimal]

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

    alimentacion = ['herbivoro', 'carnivoro', 'omnivoro']
    reproduccion = ['oviparo', 'viviparo', 'ovoviviparo']

    keys = list(db.keys())

    print('Actualizar un animal x')
    msj = 'Ingrese un numero entero: '
    llaveAnimal = comprobacion(msj, keys, 'int')

    msj = 'Desea modificar el nombre del animal [S/s] Sí [N/n] No '
    if comprobacionSN(msj):
        animal = input('Ingrese el nuevo nombre: ')
        db[llaveAnimal]['animal'] = animal

    msj = 'Desea modificar la alimentación del animal? [S/s] Sí [N/n] No '
    if comprobacionSN(msj):
        print(alimentacion)
        msj = 'Ingrese la alimentación: '
        alimentacion = comprobacion(msj, alimentacion, 'str')
        db[llaveAnimal]['alimentacion'] = alimentacion

    msj = 'Desea modificar la reproduccion del animal? [S/s] Sí [N/n] No '
    if comprobacionSN(msj):
        print(reproduccion)
        msj = 'Ingrese la reproducción: '
        reproduccion = comprobacion(msj, reproduccion, 'str')
        db[llaveAnimal]['reproduccion'] = reproduccion

    return db

# DELETE
def eliminar(db:dict)->dict:

    keys = list(db.keys())

    print('Actualizar un animal x')
    msj = 'Ingrese un numero entero: '
    llaveAnimal = comprobacion(msj, keys, 'int')

    animal = db.pop(llaveAnimal)

    print(f'Se ha eliminado el animal {animal["animal"]}')