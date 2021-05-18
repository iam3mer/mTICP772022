# Diccionarios
# {key: value}

diccionario = {}
#print(type(diccionario))

diccionario = dict()

diccionario = {'Jhonatan': 'Barrera', 1: 254.25, 0: 'cualquier cosa'}
#print(diccionario)

#print(diccionario[1]) # Se consulta a partir de la llave (key)

personas = {
    'Nataly': {
        'ciudad': 'Bogota',
        'telefono': 22455855,
        'intereses': {
            'lectura': True,
            'escritura': False,
            'deporte': 'voley'
        },
        'habilidades': {
            'programacion': True,
            'bases_de_datos': False,
            'bilingue': True
        }
    },
    'Oscar':{
        'ciudad': 'Ibague',
        'telefono': 25445585,
        'intereses': {
            'lectura': False,
            'escritura': False,
            'deporte': 'natacion'
        },
        'habilidades': {
            'programacion': False,
            'bases_de_datos': False,
            'bilingue': False
        } 
    }
}

#print(personas['Oscar']['habilidades']['deporte']) # natacion

#print(personas['Oscar']['habilidades']['bilingue'] == True) # False

personas['Oscar']['habilidades']['bilingue'] = True # actualiza el valor a True
#print(personas)

persona = {
    'ciudad': 'Pereira',
    'telefono': '31467522000',
    'intereses': {
        'lectura': True,
        'escritura': True,
        'deporte': 'Triathlon',
    },
    'habilidades': {
        'programacion': True,
        'bases_de_datos': True,
        'bilingue': True
    }
}

personas['Jhonatan'] = persona

#print(personas)

#print(personas.keys()) # dict_keys(['Nataly', 'Oscar', 'Jhonatan'])
#print(personas['Oscar'].keys()) # dict_keys(['ciudad', 'telefono', 'intereses', 'habilidades'])
#print(personas['Jhonatan']['habilidades'].keys()) # dict_keys(['programacion', 'bases_de_datos', 'bilingue'])

#print('Jhonatan' in personas.keys()) # True
#print('montañismo' in personas['Nataly']['habilidades'].keys()) # False

#print(personas.values())
#print(personas['Oscar'].values())
#print(personas['Oscar']['intereses'].values())

#print(personas)
#personas.clear()
#print(personas)

personas.update(dict(Angie = {}))
#print(personas)
personas['Angie']['ciudad'] = 'Pereira'
personas['Angie']['telefono'] = 54125455
personas['Angie']['intereses'] = {'lectura': True, 'escritura': False, 'deporte': 'Crossfit'}
personas['Angie']['habilidades'] = dict(programacion=True, bases_de_datos=True, desarrollo_web=True)
#print(personas)

del personas['Oscar']
elemento = personas.pop('Nataly')
#print(personas.keys())
#print(elemento)

# print(len(personas)) # 2