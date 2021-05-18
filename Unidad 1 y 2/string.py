# string (str)
# "Esta es una cadena de texto"
# 'Esta es otra cadena'

misionTIC = 'Este es el ciclo 1'

print(misionTIC[2])

longitudCadena = len(misionTIC)
print(longitudCadena)

print(misionTIC[longitudCadena-1])

#misionTIC[0] = 'e' # 'eEste es el ciclo 1' ?

print(misionTIC[2:6]) # te e
print(misionTIC[:6])  # Este e
print(misionTIC[6:longitudCadena]) # s el ciclo 1

print(misionTIC[12:12]) # ''
print(misionTIC[14:12]) # ''

print(dir(misionTIC))

print(misionTIC.upper()) # Pasa los caracteres a mayusculas
print(misionTIC.lower()) # Pasa los caracteres a minusculas
print(misionTIC.split()) # Separa por espacio: ['Este', 'es', 'el', 'ciclo', '1']
print(misionTIC.split('el')) # Cambia el separador: ['Este es ', ' ciclo 1']
print(misionTIC.upper().split()) # ['ESTE', 'ES', 'EL', 'CICLO', '1']
print(misionTIC.replace('E', 'e'))
print(misionTIC) # Si quiero "modificar" la cadena, misionTIC = misionTIC.replace('E', 'e')
print(misionTIC.find('colombia')) # Cuando encuentra el valor devuelve la posicion en la que inicia, sino -1
print(misionTIC.startswith('e')) # Comprueba si la cadena inicia en el valor indicado

# print(eq(misionTIC, 'Colombia')) # No se puede asumir la forma de uso
print(misionTIC.__eq__('este es el ciclo 1'))
print(misionTIC.__eq__('Este es el ciclo 1'))

contarPalabras = 'Nadie silva como silvio silva'
print(contarPalabras.count('silva'))
print(contarPalabras.count('silva', 11))
print(contarPalabras.count('silva', 8, 14))

entero = 5
flotante = 2.5
# f""
print(f"{entero} es un numero entero\n\ty {flotante} es un decimal")

# % formato, %d enteros, %f flotantes, %s string
print("\t%d es un numero entero\ny %f es un decimal" % (entero, flotante))

# format()
print("\t{} es un numero entero\ny {} es un decimal".format(entero, flotante))
