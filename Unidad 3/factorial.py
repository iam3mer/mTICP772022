def factorial(fact:int)->int:
    salida = 1
    num = 2
    while num <= fact:
        salida = salida * num
        num = num + 1
    return salida

print(factorial(4))