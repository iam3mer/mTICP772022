# int -> 5, 0x10, 0b10, 121313212132123131
# float -> 0.5, 0.5e7, 1.79e308, -1.8e308, 5e-324, 1e-325
# complex -> 05. + 2j
# boolean -> True/False
# string -> 'Hola Mundo', "Hola Mundo", '', "Hola\n Tripulantes"
# lista -> [], ['hola', 'mundo', 'x'], [2, 3, 7, 6], ['c', 3, 5.7],
#          [[3, 'url'], 'protocolo', 7]
# tupla -> (), ('hola', 'mundo', 'x'), (2, 3, 7, 6), ('c', 3, 5.7),
#          ((3, 'url'), 'protocolo', 7)
# diccionario -> {'Numero de participantes': 7, 'Entero': 10, 'Flotantes': 2.5,
#                 'Nombre de participantes': 'Tripulantes',
#                 'Lista': ['c', 3, 5.7], 'Tupla': ('hola', 'mundo', 'x'),
#                  {'Formador': 'Jhonatan', 'Profesion': 'Ingeniero de Sistemas
#                  y Computación'}}


'''
Este es un comentario de documentación
'''

'''
print('Pruebas de formatos de impresión')
print('--------------------------------')

var1 = 333
var2 = 205.5
var3 = 'Hola'


# Pruebas
print('Var1: Var2: Var3:', var1, var2, var3)
print(f'Var1: {var1} Var2: {var2} Var3: {var3}')
print('Var1: %i Var2: %.1f Var3: %s' % (var1, var2, var3)) # Formateo de impresion antiguo

print(f'Entero en bases 10, 2, 16: {var1}, {var1:b}, {var1:x}')
print(f'Entero alineado a la derecha: {var1:06}')
print(f'Real sin formato: {var2}')
print(f'Real alienado a la derecha (6 pos 0 decim): {var2:6.0f}')
print(f'Real alienado a la derecha (6 pos 3 decim): {var2:6.3f}')
print(f'Real con formato exponencial: {var2:e}')
print(f'Real con tres decimales: {var2:.3f}')
print('Real con tres decimales: %.3f' % (var2)) # Formateo de impresión antiguo
'''
bandera = True
while bandera == True:
    print("Area de un cuadrado")
    print("1. Cacular area.")
    print("2. Calcular perimetro.")
    print("3. Salir")

    opcion = input("Ingrese una opción del menu: ")
    
    if opcion == '1':
        L = float(input("Ingrese el valor del lado: "))
        area = L * L
        print(f"El area del cuadrado con lado {L} es {area}.\n")
    elif opcion == '2':
        L = float(input("Ingrese el valor del lado: "))
        perimetro = L + L + L + L
        print(f"El perimetro del cuadrado con lado {L} es {perimetro}\n")
    elif opcion == '3':
        print("\nA elegido salir del programa. Hasta luego!")
        bandera = False
    else:
        print("\nOpcion no valida.\n")