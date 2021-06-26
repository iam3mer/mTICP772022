# For

# imprimir los numeros hasta el 10
for i in range(11):
    #print(i)
    pass

# imprimir los numeros desde el 5 hasta el 20
for i in range(5,21):
    #print(i)
    pass

def printRango(x:int,y:int)->None:
    for i in range(x,y):
        print(i)
    print(i+1)

#printRango(10,20)

for i in range(5,0,-1):
    #print(i)
    pass

for i in range(5,11): 
    #print(i) # [5, 6, 7, 8, 9, 10]
    pass

numeros = [5, 6, 7, 8, 9, 10]
for i in numeros:
    #print(i)
    pass

for caracter in 'MisionTIC':
    #print(caracter)
    pass

for i in range(len(numeros)):
    #print(numeros[i])
    pass

'''
for i in range(5):
    print(f'Estoy en la iteración {i+1}')
else:
    print('Siempre se ejecuta lo que hay en esta salida.')
'''