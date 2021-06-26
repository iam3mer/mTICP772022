# Datatypes ------------------------------------------
# Enteros (int)
# 5
# 21
# -54
print(type(42))

# Flotantes (float)
# 554.25
# -54.02
# 547.1
print(type(0.25))

# String (str)
print(type('Hola Mundo'))
print(type("Hola Mundo"))
print(type('''Hola Mundo'''))
print(type("""Hola Mundo"""))
print(type(''))

# Booleanos (bool)
# True -> ...-3, -2, -1, 1, 2, 3...
# False -> 0
print(type(True))
print(type(False))

# Variables ---------------------------------------
nombreClave = 'Almacena datos, colecciones' # Camel Case
nombre_clave = 'Almacena datos, colecciones' # Snake Case
NombreClave = 'Almacena datos, colecciones' # Pascal Case

var1, var2, var3 = 1, 2, 3

print(type(nombreClave))
nombreClave = 25
print(type(nombreClave))
print(nombreClave)

numeroSTR = '25'
print(type(numeroSTR))
numero = int(numeroSTR)
print(type(numero))
print(type(numeroSTR))
numero = float(numeroSTR)
print(type(numero))
print(numero)

print(int(True))
print(int(False))

print(chr(47))
print(ord('/'))

# Colecciones --------------------------------------------
# Lista (list)
lista_vacia = []
print(type(lista_vacia))

mi_lista = [345,456,96,5476,456,36,345.34,3434.346,['ter','ert','ertyg']]
print(mi_lista[0])
print(mi_lista[1])
# print(mi_lista[9]) # Error, indice fuera del rango
print(mi_lista[8])
print(mi_lista[len(mi_lista)-1])
print(mi_lista[8][2])

print(mi_lista[7:58])
print(mi_lista[::-1]) # Invierte el orden de los elementos de la coleccion
print(mi_lista[:-1]) # Omite el ultimo elemento de la coleccion

mi_lista[8][2] = 'P77'
print(mi_lista)

print(dir(mi_lista))

mi_lista.append('Otra cadena')
print(mi_lista)
ultimo_elemento = mi_lista.pop()
print(mi_lista)
print(ultimo_elemento)
mi_lista.pop(7)
print(mi_lista)
mi_lista.insert(0,[23,2354,235,245,4])
print(mi_lista)

print(lista_vacia.__sizeof__())
print(mi_lista.__sizeof__())

# Tuplas (tuple)
tupla_vacia = ()
una_tupla = (345,56,476,54687,65789,768)
otra_tupla = 345,56,476,54687,65789,768
print(type(tupla_vacia), type(una_tupla), type(otra_tupla))

print(dir(tupla_vacia))
print(otra_tupla[0])
# otra_tupla[0] = 234 # No se puede
print(otra_tupla[len(otra_tupla)-1])
print(otra_tupla[1:5])

print((345,5463,465) > (345,674,548))

# Conjuntos (set)
un_set = {234,2345,345,6356,234,456,2345,56,57,34,345,456,3456,45,345}
print(type(un_set))
# print(un_set[0]) # No se puede

print(dir(un_set))

print(len(un_set))
print(un_set)
print(un_set.pop())
print(un_set)

otro_set = {345,363,636,4756,33,453245,246,535746,345,32,34,345}

union = un_set.union(otro_set)
print(union)
interseccion = otro_set.intersection(un_set)
print(interseccion)
diferencia1 = un_set.difference(otro_set)
diferencia2 = otro_set.difference(un_set)
print(diferencia1)
print(diferencia2)

# Diccionarios (dict)
# {key: value}
diccionario_vacio = {}

otro_diccionario = {
    'nombre': 'Jhonatan',
    'apellido': 'Barrera',
    'adicional': ['Risaralda', 'Pereira', {'profesion': 'Ingeniero de Sistemas y Computación',
                                           'universidad': 'Universidad Tecnológica de Pereira'}]
}

print(otro_diccionario['adicional'][2]['profesion'])

print(dir(otro_diccionario))

un_elemento = otro_diccionario['adicional'][2].pop('universidad')
print(un_elemento)
print(otro_diccionario)

print(list(otro_diccionario.keys()), list(otro_diccionario.values()))

print(list(otro_diccionario.items()))

otro_diccionario['Nueva llave'] = 85
print(otro_diccionario)
otro_diccionario['Nueva llave'] = 'Nuevo valor'
print(otro_diccionario)

otro_diccionario.update(nueva_llave = {'codigo': 'FP01', 'nombre': 'Fundamentos de programacion'})
print(otro_diccionario)

# Condicionales ---------------------------------------------
if otro_diccionario['Nueva llave'] == 'Nuevo valor':
    print('Son iguales')
    # instruccion 2
    # instruccion 3
#instruccion 4

if otro_diccionario['Nueva llave'] == 85:
    print('Son iguales')
else:
    print('No son iguales')

numero1 = [234,345,45,3564]
numero2 = [345,45,634,5]

if numero1[0] == numero2[0]:
    print('Son iguales')
elif numero1[0] < numero2[0]:
    print(f'{numero1[0]} es menor que {numero2[0]}')
else:
    print(f'{numero1[0]} es mayor que {numero2[0]}')

if True:
    print('Esto siempre se va a mostrar (Siempre es verdadero)')

if False:
    pass
else:
    print('Siempre se va ha mostrar (Nunca sera verdadero)')

# Ciclos (for, while)
for item in numero2:
    print(item, end=' ')
print()
for i in range(len(numero2)):
    print(numero2[i], end=' ')
print()
for key in otro_diccionario:
    print(otro_diccionario[key])

for k, v in otro_diccionario.items():
    print(k, v)

band = True
contador = 0
while band:
    contador = contador + 1
    print(contador, end=' ')
    if contador == 10:
        band = False
        # break
print()
i = 0
while i < len(numero2):
    if numero1[i] == numero2[i]:
        print('Son iguales')
    elif numero1[i] < numero2[i]:
        print(f'{numero1[i]} es menor que {numero2[i]}')
    else:
        print(f'{numero1[i]} es mayor que {numero2[i]}')
    i = i + 1

for i in range(len(numero2)):
    if numero1[i] == numero2[i]:
        print('Son iguales')
    elif numero1[i] < numero2[i]:
        print(f'{numero1[i]} es menor que {numero2[i]}')
    else:
        print(f'{numero1[i]} es mayor que {numero2[i]}')

print('-------------------------------------------------------')
# Funciones
def comparaNum(num1:int,num2:int)->str:
    if num1 == num2:
        return 'Son iguales'
    elif num1 < num2:
        return f'{num1} es menor que {num2}'
    else:
        return f'{num1} es mayor que {num2}'

print(comparaNum(34,567),'\n')

for i in range(len(numero2)):
    print(comparaNum(numero1[i], numero2[i]))
print()

i = 0
while i < len(numero2):
    print(comparaNum(numero1[i], numero2[i]))
    i = i + 1