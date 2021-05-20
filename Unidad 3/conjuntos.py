# Conjuntos
conjunto = set() # Es mutable
conjunto = {2345,3453,34534,345,'sdfsdf', (3453,'dsfgd')}
#print(conjunto)

conjunto.pop()
#print(conjunto)
conjunto.pop()
#print(conjunto)

conjunto.add((234234,3435465,567567,345))
#print(conjunto)

a = {1,2,3,4,5,6,7}
b = {4564,87,3,4,6,567,5678}

#print(a.union(b))
#print(a.intersection(b))
#print(a.difference(b))
#print(b.difference(a))

#print(b.isdisjoint(a))

numeros = [234234,234,23542,52,543]
print(numeros)
numeros = set(numeros)
print(numeros)
numeros = list(numeros)
print(numeros)

# fronzenset() # No es mutable.