# Tuplas

tuplaVacia = ()
tuplaVacia = tuple()

unaTupla = 3, 5, 8

#print(unaTupla[1]) # 5

#unaTupla[0] = 10 # Esto no se puede hacer

numeros = tuple([234,2342,3545])
#print(numeros)

nombres = ('Camilo', 'Leandro', 'angie', 'Giovanny', 'Andrey', 'Samuel')

numeros = numeros + nombres
#print(numeros)

#print((0,5,9) > (0,5,10))

listaNombres = list(nombres)
#print(listaNombres)

diccionario = {('Pereira', 'Cali'): 3, ('Pereira', 'Bogota'): 9}
print(list(diccionario.keys())[0][1])
print(f"Entre {list(diccionario.keys())[1][0]} y {list(diccionario.keys())[1][1]} hay {diccionario[('Pereira', 'Bogota')]} horas")

