from numpy import random as r
from numpy.core.fromnumeric import size

# Ejecutar desde consola

print(
    r.choice(['Mayte', 'Nicolas', 'Johan', 'Genny'],
                    size = r.choice([1,2], p = [0.1,0.9]),
                    p = [0.5, 0.2, 0.2, 0.1],
                    replace = False))