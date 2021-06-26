# lista
 
listaVacia = []
listaVacia = list()

otraLista = [23423,4234,234,2342,3542,352.5435,23422,[45345,'cadena'], 234]

#print(otraLista[2])

otraLista.append('otra cadena')
#print(otraLista)

otraLista.append(45)
#print(otraLista)

otraLista.extend('5')
#print(otraLista)

otraLista.extend('programación')
#print(otraLista)

otraLista.extend('45')
#print(otraLista)

otraLista.append([345,34534,34653])
#print(otraLista)

otraLista.extend([345,34534,34653])
#print(otraLista)

otraLista[0] = 'Hola'
#print(otraLista)

otraLista.insert(1,'Mundo')
#print(otraLista)

elemento = otraLista.pop(4)
#print(otraLista)
#print(elemento)

otraLista.remove(23422)
#print(otraLista)

#print(otraLista[6][1])

otraLista[6].remove('cadena')
#print(otraLista)

otraLista[6].append('remplazo')
#print(otraLista)

otraLista.reverse()
#print(otraLista)

numeros = [34345,456,475,6856,7986,98745,654,75,7867,845]
numeros.sort()
#print(numeros)

nombres = ['Camilo', 'Leandro', 'angie', 'Giovanny', 'Andrey', 'Samuel']
nombres.sort()
#print(nombres)

matriz = [[3453,34534,53456],[3456,756743,853],[853,3468,342]]

#print(matriz[0][2])
#print(matriz[1][2])
#print(matriz[2][2])
#print(matriz[2][0],[1][2],[2][2])

'''
for i in range(len(matriz)):
    print(matriz[i][2])
print('-----')
for i in matriz:
    print(i[2])
'''

cubo = [[['a', 'e'], ['b', 'f']], [['c', 'h'], ['d', 'g']]]

print(cubo[0]) # [['a', 'e'], ['b', 'f']]
print(cubo[0][1]) # ['b', 'f']
print(cubo[0][1][1]) # f
