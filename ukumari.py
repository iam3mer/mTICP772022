def desperdicio_de_gaseosa(amigo_1:dict, amigo_2:dict, amigo_3:dict, capacidad_boton:float)->str:

    # Que vaso se reboso ?
    reboso1 = (amigo_1['capacidad_actual'] + capacidad_boton) - amigo_1['capacidad_vaso']
    reboso2 = (amigo_2['capacidad_actual'] + capacidad_boton) - amigo_2['capacidad_vaso']
    reboso3 = (amigo_3['capacidad_actual'] + capacidad_boton) - amigo_3['capacidad_vaso']

    s1 = reboso1 > 0 
    s2 = reboso2 > 0 
    s3 = reboso3 > 0 

    # Que vaso se llena primero ?
    amigo_1['vaso1'] = amigo_1['capacidad_vaso'] - amigo_1['capacidad_actual'] # 3
    amigo_2['vaso2'] = amigo_2['capacidad_vaso'] - amigo_2['capacidad_actual'] # 2
    amigo_3['vaso3'] = amigo_3['capacidad_vaso'] - amigo_3['capacidad_actual'] # 4
    
    # Hora de retornar
    if s1 and s2 and s3:
        primero = min(amigo_1['vaso1'], amigo_2['vaso2'], amigo_3['vaso3'])
        if amigo_1['vaso1'] == primero:
            return amigo_1['nombre']
        elif amigo_2['vaso2'] == primero:
            return amigo_2['nombre']
        elif amigo_3['vaso3'] == primero:
            return amigo_3['nombre']


llena = 5.7

amigo1 = {
    'nombre': 'Juan',
    'capacidad_vaso': 10,
    'capacidad_actual': 7
}

amigo2 = {
    'nombre': 'Maria',
    'capacidad_vaso': 10,
    'capacidad_actual': 8
}

amigo3 = {
    'nombre': 'Felipe',
    'capacidad_vaso': 10,
    'capacidad_actual': 6
}

print(desperdicio_de_gaseosa(amigo1, amigo2, amigo3, llena))
