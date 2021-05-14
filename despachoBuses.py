def despacho_buses(personas_bus: int, personas_estacion: int)->bool:
    """ La estación de Megabus
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """

    # Capacidad Bus 150
    # Sobre cupo mayor a 150, hasta 200
    # Usuarios se suben a bús con sobrecupo sí, en plataforma hay 40 o más
    # personas
    # Se despacha un nuevo bus si el bus saliente va con sobrecupo o
    # si en la plataforma quedán 50 o mas personas

    CAPACIDAD = 150
    PLATAFORMA = 50

    cupo = CAPACIDAD - personas_bus
    #cupo = 150 - 50 = 100

    enPlataforma = personas_estacion - cupo
    #enPlataforma = 200 - 100 = 100

    #print(cupo, enPlataforma)

    if personas_bus > CAPACIDAD or enPlataforma >= PLATAFORMA:
        return True
    else:
        return False

print(despacho_buses(50,200)) # True, se suben 150 personas y quedan 50
print(despacho_buses(170,10)) # True, no se sube ninguna y quedan 10
print(despacho_buses(50,10))  # False, se suben 10 usuarios, no sc
print(despacho_buses(50,50))  # False, se suben 50 usuarios, no sc
print(despacho_buses(140,20)) # False, se suben 10 usuarios, quedan 10, nsc
print(despacho_buses(149,30)) # False, se sube 1, quedan 29 y no despacha
print(despacho_buses(100,90)) # False, se suben 90, hay sc
print(despacho_buses(150,30)) # False, no se sube nadie, quedan 30, n sc
print(despacho_buses(200,50)) # True, no se sube nadie, qeudan 50, sc