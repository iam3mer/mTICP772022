dinos={
'Ornithischia':{
'Tireoforos':[('Chialingosaurus',150),('Ankylosaurus'
,6800),('Scelidosaurus',270)],
'Neornitisquios':[('Iguanodon',4200),('Pachycephalosaurus',820),('Triceratops',7800)]
},
'Saurischia':{
'Teropodos':[('Tyrannosaurus',6700),('Velociraptor',
15),('Gigantoraptor',1900),('Archaeopterix',1)],
'Sauropodomorfos':[('Saturnalia',10),('Apatosaurus',
20200),('Diplodocus',113000)]
}
}

from functools import reduce

def promedio(datos:list)->int:
    promedio = round(reduce(lambda x, y: x + y, datos) / len(datos), 2)
    return promedio

def busquedaDinos(opt:int,db:dict,grupo_principal:str=''):
    
    promedios = {}

    try:
        if opt == 2 and grupo_principal != '':
            solucion = 'La opción no recibe grupo principal'

        elif opt == 2:
            for grupo_principal in db:
                dinosaurios = []
                tipoDinosaurios = db[grupo_principal]
                for dinosaurio in tipoDinosaurios:
                    for i in range(len(tipoDinosaurios[dinosaurio])):
                        dinosaurios.append(tipoDinosaurios[dinosaurio][i][1])
                promedios[grupo_principal] = promedio(dinosaurios)
            solucion = promedios

        elif opt == 3:
            tipoDinosaurios = db[grupo_principal]
            for dinosaurio in tipoDinosaurios:
                dinosaurios = []
                for i in range(len(tipoDinosaurios[dinosaurio])):
                    dinosaurios.append(tipoDinosaurios[dinosaurio][i][1])
                promedios[dinosaurio] = promedio(dinosaurios)
            solucion = promedios

        elif opt == 1:
            dinoMax = ('',0)
            subGrupos = db[grupo_principal]
            for subGrupo in subGrupos:
                dinosaurios = subGrupos[subGrupo]
                for dinosaurio in dinosaurios:
                    if dinosaurio[1] > dinoMax[1]:
                        dinoMax = dinosaurio
            solucion = dinoMax

        else:
            solucion = 'La opción no es valida'
    
    except:
        solucion = 'La opción ingresada requiere el nombre de un grupo principal valido'

    return solucion

print(busquedaDinos(1, dinos))
print(busquedaDinos(3, dinos, 'Saurischia'))
print(busquedaDinos(2, dinos))
print(busquedaDinos(1, dinos, 'Ornithischia'))
print(busquedaDinos(7, dinos))