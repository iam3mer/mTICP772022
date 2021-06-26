# CRUD (Cread, Read, Update, Delete)

estructuraAnimales = {
    'animal': 'nombre del animal',
    'estructura': {
        'vertebrado': ['mamiferos', 'aves', 'peces', 'reptiles', 'anfibios'],
        'invertebrado': ['poriferos', 'cnidarios', 'moluscos', 'anelidos', 'artropodos']
    },
    'alimentacion': ['herbivoro', 'carnivoro', 'omnivoro'],
    'reproduccion': ['oviparo', 'viviparo', 'ovoviviparo']
}


dbAnimales = {
    1: {
        'animal': 'araña',
        'estructura': {
            'vertebrado': False,
            'invertebrado': True,
            'tipo': 'artropodo'
        },
        'alimentacion': 'carnivoro',
        'reproduccion': 'oviparo'
    }
}


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

    db[llave] = animal

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


#dbActualizada = crear(dbAnimales)
#consultar(dbActualizada)

#consultar(dbAnimales)
#dbActualiza = actualizar(dbAnimales)
#consultar(dbAnimales)

eliminar(dbAnimales)