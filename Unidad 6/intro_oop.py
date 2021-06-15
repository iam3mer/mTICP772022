# Clases y Objetos
# Un objeto es una instancia de una clase

nombre = str('Jhonatan')
# print(type(nombre))

def fun():
    pass

# print(type(fun))

# Sintaxis basica para una clase
class Chocolate:
    pass

chocolate_1 = Chocolate()
# print(type(chocolate_1))
# print(chocolate_1)

chocolate_2 = Chocolate()
# print(chocolate_2)

# print(Chocolate)
# print(type(chocolate_2))
# print(chocolate_2.__class__)

# print(Chocolate.__name__)
# print(type(chocolate_2).__name__)
# print(chocolate_2.__class__.__name__)

# Atributos y Métodos

chocolate_3 = Chocolate()
chocolate_3.sabor = 'vainilla'
chocolate_3.color = 'blanco'

# print(f'El sabor del chocolate es de {chocolate_3.sabor} y es de color {chocolate_3.color}')

class Chocolate:
    vainilla = True

chocolate = Chocolate()

if chocolate.vainilla:
    print('El chocolate tiene sabor a Vainilla')
else:
    print('El chocolate no tiene sabor a Vainilla')

print(chocolate.vainilla)
    
chocolate.vainilla = False

if chocolate.vainilla:
    print('El chocolate tiene sabor a Vainilla')
else:
    print('El chocolate no tiene sabor a Vainilla')

Chocolate.vainilla = False

chocolate = Chocolate()

if chocolate.vainilla:
    print('El chocolate tiene sabor a Vainilla')
else:
    print('El chocolate no tiene sabor a Vainilla')