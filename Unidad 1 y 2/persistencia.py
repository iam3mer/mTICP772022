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
n = contadorFun(n)
print(n)