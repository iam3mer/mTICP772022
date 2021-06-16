# Clases y Objetos
# Un objeto es una instancia de una clase

from typing import SupportsAbs


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
    
# chocolate.vainilla = False

# if chocolate.vainilla:
#     print('El chocolate tiene sabor a Vainilla')
# else:
#     print('El chocolate no tiene sabor a Vainilla')

Chocolate.vainilla = False

chocolate = Chocolate()

if chocolate.vainilla:
    print('El chocolate tiene sabor a Vainilla')
else:
    print('El chocolate no tiene sabor a Vainilla')

# Metodos
class Chocolate:
    vainilla = True

    def saludar(soy_el_propio_Objeto):
        print('Hola, soy un delicioso chocolate!')
        print(soy_el_propio_Objeto)

chocolate = Chocolate()
chocolate.saludar()
# Chocolate.saludar()
print(chocolate)

class Chocolate:
    vainilla = True

    def sabor(self):
        self.vainilla = False

chocolate = Chocolate()
chocolate.sabor()
print(chocolate.vainilla)
print()

# Constructor
class Chocolate:
    vainilla = True

    def __init__(self, relleno, color, cuadritos):
        self.relleno = relleno
        self.color = color
        self.cuadritos = cuadritos
        print(f'Soy un chocolate recien salido del molde! ({self})')

    def __del__(self):
        print(f'Se acaba de destruir el chocolate! ({self})')

    def __str__(self):
        return f'Tengo relleno de {self.relleno} y color {self.color}'

    def __len__(self):
        return self.cuadritos

chocolate_1 = Chocolate('mani', 'blanco', 6)
del(chocolate_1)

chocolate_2 = Chocolate('almendra', 'fucsia', 10)
# chocolate_2.__del__()

print(chocolate_2)
print(str(chocolate_2))
print(chocolate_2.__str__())

print(chocolate_2.__len__())
print(len(chocolate_2))

# Encapsulación

class Encap:
    __atributo_privado = 'Soy un atributo privado y no puedo ser alcanzado desde el exterior.'

    def __metodo_privado(self):
        print('Soy un metodo privado, soy inalcanzable')

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()


objeto = Encap()
# print(objeto.__atributo_privado)
# objeto.__metodo_privado()

print(objeto.atributo_publico())
objeto.metodo_publico()

# Herencia
class Producto:

    def __init__(self, ref, tipo, nombre, pvp, des, isbn=None, autor=None):
        self.referencia = ref
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.des = des
        self.isbn = isbn
        self.autor = autor

carro = Producto('Car01', 'Comfortline', 'Nivus', 78990000, 'La nueva Nivus de WV')

print(carro)
print(carro.tipo)

class Producto:

    def __init__(self, ref, tipo, nombre, pvp, des):
        self.referencia = ref
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.des = des

    def __str__(self):
        return f'REFERENCIA\t {self.referencia}\n' \
               f'TIPO\t {self.tipo}\n' \
               f'NOMBRE\t {self.nombre}\n' \
               f'PVP\t {self.pvp}\n' \
               f'DESCRIPCION\t {self.des}\n'

carro = Producto('Car01', 'Comfortline', 'Nivus', 78990000, 'La nueva Nivus de WV')

class Libro(Producto):
    isbn = ''
    autor = ''

    def __str__(self):
        return f'REFERENCIA\t {self.referencia}\n' \
               f'TIPO\t {self.tipo}\n' \
               f'ISBN\t {self.isbn}\n' \
               f'NOMBRE\t {self.nombre}\n' \
               f'AUTOR\t {self.autor}\n' \
               f'DESCRIPCION\t {self.des}\n' \
               f'PVP\t {self.pvp}\n'

libro = Libro('Lib01', 'Aventura', 'Viaje al centro de la Tierra', 65000, 'Viajeros intrépidos descubren nuevos mundos subterráneos')
libro.autor = 'Julio Verne'
libro.isbn = 'dgfsfdg67s9df'

print(libro)

# Polimorfismo
def descuento(producto, porcentaje):
    producto.pvp = producto.pvp - (producto.pvp * porcentaje / 100)

print(carro)
descuento(carro, 15)
print(carro)