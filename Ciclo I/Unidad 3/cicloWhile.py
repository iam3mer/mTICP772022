# While

'''
n = 0
while n <= 10:
    print(n)
    n = n + 2 # Avance incremental
else:
    print("Termino el While") # Esto siempre se imprime

print('-----')
n = 10
while n >= 0:
    print(n)
    n = n - 2 # Avance decremental

# Ojo esto genera un ciclo infinito
n = 1
while n > 0:
    print(n)
    n = n + 1

# Romper un ciclo infitino
n = 10
while True:
    if n == 0:
        break
    print(n)
    n = n - 1

# Saltarse sentencias
n = 0
while n < 10:
    n = n + 1
    if n % 2 != 0:
        continue
    print(n)
'''
