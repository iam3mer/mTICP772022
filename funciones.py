""" print('A continuación un print sin parametros')
print()
print('A continuacion un print con end modificado ('')')
print(end='')

var1 = 3
var2 = 7
var3 = 2
var4 = 4
var5 = 5

print("Los valores son:",var1, var2, var3, var4, var5)
print('El valor máximo es:')
maximo = max(var1, var2, var3, var4, var5)
print(maximo)

print('El valor mínimo es:')
minimo = min(var1, var2, var3, var4, var5)
print(minimo)

x = range(5)
print(x) """

# Para crear una función
'''
def func(parámetros, parámetros, ...):
    # Bloque de código <-- Identado
    return
'''

# Llamar a la función
'''
func(argumento, argumento, ...)
'''

# Almacenar retorno en una variable (si hay return)
'''
variable = func(argumento, argumento, ...)
'''

def multiplicacion(x, y):
    return x * y

a = 10
b = 5
#print(multiplicacion(a,b))
#resultado = multiplicacion(a, b)
#print(resultado)

def suma(x, y):
    print(x+y)

#resultado2 = suma(a, b)

#print(resultado2)