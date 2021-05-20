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
            tipo = comprobacion(msj, vertebrados)
            break
        elif estructura == '2':
            print(invertebrados)
            tipo = comprobacion(msj, invertebrados)
            break

    print(alimentacion)
    msj = 'Ingrese el tipo de alimentacion de los valores presentados: '
    seleccionAlimentacion = comprobacion(msj, alimentacion)

    msj = 'Ingrese el tipo de reproduccion de los valores presentados: '
    print(reproduccion)
    seleccionReproduccion = comprobacion(msj, reproduccion)

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

def comprobacion(msj:str, lista:list)->str:
    while True:
        entra = input(msj)
        for item in lista:
            if entra == item:
                return entra


print(crear(dbAnimales))