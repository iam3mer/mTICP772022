from matplotlib import colors
import matplotlib.pyplot as plt
from random import random, randrange

from numpy import place

x1 = [random() for _ in range(7)]
y1 = [random() for _ in range(7)]

x2 = [random() for _ in range(7)]
y2 = [random() for _ in range(7)]

print(x1,y1)

# plt.plot(x1,y1, color='green', linewidth=2, label='Serie 1')
# plt.plot(x2,y2, color='blue', linewidth=3, label='Serie 2')
# plt.title('Mi primer grafica de Serie con Matplotlib')
# plt.xlabel('Axis X')
# plt.ylabel('Axis Y')
# plt.legend()
# plt.grid()
# plt.show()

x1 = [randrange(2,10,3) for _ in range(7)]
y1 = [randrange(6,20,2) for _ in range(7)]

x2 = [randrange(12,26,3) for _ in range(7)]
y2 = [randrange(4,18,3) for _ in range(7)]

# plt.bar(x1,y1, color='orange', label='Barra 1')
# plt.bar(x2,y2, color='red', label='Barra 2')
# plt.title('Grafica de Barras')
# plt.xlabel('Axis X')
# plt.ylabel('Axis Y')
# plt.legend()
# plt.grid()
# plt.show()

Datos = [20,22,21,20,23,25,28,40,22,23,22,15,16,18,18,19,21,22,24,4,12,17,17,22,30,]
Rangobin = [0,10,20,20,30,40]

# plt.hist(Datos, Rangobin, histtype='bar', rwidth=0.8, color='lightgreen')
# plt.title('Histograma')
# plt.xlabel('Axis X')
# plt.ylabel('Axis Y')
# plt.show()

# plt.scatter(x1,y1, color='red', label='Puntos 1')
# plt.scatter(x2,y2, color='blue', label='Puntos 2')
# plt.title('Scatter')
# plt.xlabel('Axis X')
# plt.ylabel('Axis Y')
# plt.grid()
# plt.show()

# plt.pie(x1, labels=['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7'], startangle=90, shadow=True, explode=(0.5,0,0,0.2,0,0,0), autopct='%1.1f%%')
# plt.show()

plt.figure(figsize=(30,20))

plt.subplot2grid((2,2),(0,0))
plt.plot(x1,y1, color='green', linewidth=2, label='Serie 1')
plt.title('Grafica 1')

plt.subplot2grid((2,2),(0,1))
plt.bar(x1,y1, color='orange', label='Barra 1')
plt.title('Grafica 2')

plt.subplot2grid((2,2),(1,0))
plt.scatter(x1,y1, color='red', label='Puntos 1')
plt.title('Grafica 3')

plt.subplot2grid((2,2),(1,1))
plt.pie(x1, labels=['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7'], startangle=90, shadow=True, explode=(0.5,0,0,0.2,0,0,0), autopct='%1.1f%%')
plt.title('Grafica 4')
plt.legend()
plt.grid()
plt.show()