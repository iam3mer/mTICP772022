from pprint import pprint as pp

# Guardar y Leer archivos con Pandas
import pandas as pd

data = {
    'primer_nombre': ['Camilo', 'Genny', 'Johan', 'Mayte', 'Harold'],
    'apellidos': ['Suarez', 'Calderon', 'Salazar', 'Carvajal', 'Sequeda'],
    'edad': [19, 20, 22, 19, 21],
    'tarea_1': [4,4.6,5,3.7,4],
    'tarea_2': [3.5,'?',4,'4.5','?']
}

dataDF = pd.DataFrame(data) # Convierte el diccionario en un DataFrame

#print(datdataDFaCSV)
#print()

# DF a CSV
dataDF.to_csv('infoTripulantes.csv') # Guardo el DataFrame como un CSV

leerDF = pd.read_csv(
    'infoTripulantes.csv',
    skiprows=1, # Ignora la primer fila del archivo
    names=['ID', 'Primer Nombre', 'Apellido', 'Edad', 'Reto 1', 'Reto 2'], # Nombra cada una de las columnas
    #index_col='ID',
    index_col=['Primer Nombre', 'Apellido'], # Establece los index del DF
    na_values=['?'])

#print(leerDF)

# DF a XLSX
dataDF.to_excel('infoTripulantes.xlsx', sheet_name='Tripulantes')

dfXLSX = pd.read_excel(
    'infoTripulantes.xlsx',
    sheet_name='Tripulantes',
    index_col=0)
#print(dfXLSX)

# Manipulación de archivos con Python

# Modos de lectura
# r : Lectura.
# w : Escritura. Remplaza contenido en el archivo. Si el archivo no existe lo crea.
# a : Escritura. Conserva el contenido. Añade datos al final.
# r+, w+, a+
# rb, wb, ab, rb+,. wb+, ab+

datos = ['Estamos estudiando la Unidad 5', 'Aprendemos como manipular archivos']

fichero = open('documento.txt', 'a+')
#print(fichero)

for line in datos:
    #fichero.write(line)
    #print(line, file=fichero)
    pass

#fichero.writelines('%s\n' % s for s in datos)

fichero = open('documento.txt', 'r')
#lines = fichero.readlines()
#print(lines)
#for line in lines: 
    #print(line, end='')

lines = list(fichero)
#print(lines)

lines = [line.rstrip('\n') for line in lines]
#print(lines)

# Leer linea a linea
lines = []

for line in fichero:
    lines.append(line)

fichero.close()

# Archivos JSON
import json

datos = {}
datos['tripulante'] = []

datos['tripulante'].append({
    'primer_nombre': 'Camilo',
    'apellido': 'Suarez',
    'edad': 19,
    'notas': [4,3.5]
})

datos['tripulante'].append({
    'primer_nombre': 'Genny',
    'apellido': 'Calderon',
    'edad': 20,
    'notas': 4.6
})

datos['tripulante'].append({
    'primer_nombre': 'Johan',
    'apellido': 'Salazar',
    'edad': 22,
    'notas': [5,4]
})

with open('infoTripulantes.json', 'w') as fichero:
    json.dump(datos, fichero, indent=4, ensure_ascii=False, sort_keys=True)

with open('infoTripulantes.json') as fichero:
    infoJSON = json.load(fichero)
    #pp(infoJSON)

# Consumir una API
import requests

respuesta = requests.get('http://ip-api.com/json/208.80.152.201')
respuestaJSON = json.loads(respuesta.content)
pp(respuestaJSON)