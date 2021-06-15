from pprint import pprint as pp

clientes = [
    {'numCuenta': 552545555, 'nombresTitular': 'Maria Teresa', 'apellidosTitular': 'Carvajal Galvis'},
    {'numCuenta': 564852415, 'nombresTitular': 'Jair Andrey', 'apellidosTitular': 'Salcedo Arevalo'},
    {'numCuenta': 547854545, 'nombresTitular': 'Cristian Camilo', 'apellidosTitular': 'Suárez Bolaños'}
]

# Muestra Cliente (numCuenta)
def consulta_cliente(numCuenta: int, db:list):
    for cliente in db:
        if numCuenta == cliente['numCuenta']:
            print(f'{cliente["nombresTitular"]} {cliente["apellidosTitular"]}')
            return
    print('El numero de cuenta no existe.')

# Eliminar Cliente (numCuenta)
def eliminar_cuenta(numCuenta: int, db:list):
    for i, cliente in enumerate(db):
        if numCuenta == cliente['numCuenta']:
            del(db[i])
            print(str(cliente), '> ELIMINADO')
            return
    print('El numero de cuenta no existe.')

print('-----------------Listar Clientes-----------------')
pp(clientes)

print('-----------------Mostrar Cliente-----------------')
consulta_cliente(545635636, clientes)
consulta_cliente(564852415, clientes)

print('----------------Elimininar Cuenta----------------')
eliminar_cuenta(547854545, clientes)
eliminar_cuenta(548557585, clientes)

print('-----------------Listar Clientes-----------------')
pp(clientes)

print()

# ORIENTADA A OBJETOS

# Estructura para los clientes
class Cliente:

    def __init__(self, numCuenta, nombresTitular, apellidosTitular):
        self.numCuenta = numCuenta
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular

    def __str__(self):
        return f'{self.nombresTitular} {self.apellidosTitular}'

# Estructura para las cuentas
class Cuenta:

    def __init__(self, clientes = []):
        self.clientes = clientes
    
    def consulta_cliente(self, numCuenta:None):
        for cliente in self.clientes:
            if numCuenta == cliente.numCuenta:
                print(cliente)
                return
        print('La cuenta no existe.')

    def eliminar_cuenta(self, numCuenta:None):
        for i, cliente in enumerate(self.clientes):
            if numCuenta == cliente.numCuenta:
                del(self.clientes[i])
                print(str(cliente),'> ELIMINADO')
                return
        print('La cuenta no existe.')

mayte = Cliente(numCuenta=552545555, nombresTitular='Maria Teresa', apellidosTitular='Carvajal Galvis')
jair = Cliente(numCuenta=564852415, nombresTitular='Jair Andrey', apellidosTitular='Salcedo Arevalo')
camilo = Cliente(numCuenta=547854545, nombresTitular='Cristian Camilo', apellidosTitular='Suárez Bolaños')

cuentas = Cuenta(clientes=[mayte, jair, camilo])

print('-------------------Listar Clientes-------------------')
print(cuentas.clientes)

print('-------------------Mostrar Cliente-------------------')
cuentas.consulta_cliente(552545555)
cuentas.consulta_cliente(584558524)

print('------------------Eliminar Cuenta--------------------')
cuentas.eliminar_cuenta(547854545)
cuentas.eliminar_cuenta(657415584)

print('-------------------Listar Clientes------------------')
print(cuentas.clientes)