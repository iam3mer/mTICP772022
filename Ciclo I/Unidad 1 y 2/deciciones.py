'''
if True:
    # acciones

if True:
    pass
else:
    # acciones
'''

# 'D': 0 - 1.9
# 'I': 2 - 2.9
# 'A': 3 - 3.9
# 'S': 4 - 4.8
# 'E': 4.9 - 5

# Decisiones simples / secuenciales
def notas1(nota: float)->str:
    if nota >= 0 and nota <= 1.9:
        print('D')
    if nota >= 2 and nota <= 2.9:
        print('I')
    if nota >= 3 and nota <= 3.9:
        print('A')
    if nota >= 4 and nota <= 4.8:
        print('S')
    if nota >= 4.9 and nota <= 5:
        print('E')

#notas1(4.5)

# Decisiones en Cascada
def notas2(nota: float)->str:
    if nota >= 0 and nota <= 1.9:
        print('D')
    elif nota >= 2 and nota <= 2.9:
        print('I')
    elif nota >= 3 and nota <= 3.9:
        print('A')
    elif nota >= 4 and nota <= 4.8:
        print('S')
    elif nota >= 4.9 and nota <= 5:
        print('E')

#notas2(2.5)

#Decisiones anidadas
def numeros(num:int)->str:

    if num > 0:
        #positivo
        #num >= 10 and num < 100
        if 10 <= num < 100:
            print(f"{num} es de dos digitos.")
    else:
        #negativo
        if num <= -100 and num > -1000:
            print(f"{num} es de tres digitos.")

numeros(50)