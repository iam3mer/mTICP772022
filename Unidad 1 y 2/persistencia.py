def funcion(num:int)->int:
    num = num * 2
    return num

num = 10
#print(funcion(num)) # 20
#print(num) # 10

num = funcion(num)
#print(num) # 20

def contadorFun(n:int)->int:
    n = n + 1
    return n

n = 0
n = contadorFun(n)
n = contadorFun(n)
n = contadorFun(n)
n = contadorFun(n)
n = contadorFun(n) # persiste el valor de n que se calcula en la función
#print(n)

nombres = ['Cristian', 'Andrea', 'Harold', 'Samuel']
def agregaElemento(elemento:str, lista:list)->str:
    lista.append(elemento)
    return lista

agregaElemento('Jair', nombres)
print(nombres)