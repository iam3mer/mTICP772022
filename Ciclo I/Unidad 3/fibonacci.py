# serie de fibonacci hasta valor menor que "n"
def fibonacci(n:int=50)->int:
    n1, n2 = 0, 1
    while n2 < n:
        print(n2)
        n1, n2 = n2, n1 + n2

#fibonacci()

# Fibonacci a partir de valor mayor que "num"
def fibonacciModificado(num:int=0,n:int=50)->int:
    n1, n2 = 0, 1
    while n2 < n:
        if n2 > num:
            print(n2)
        n1, n2 = n2, n1 + n2

fibonacciModificado(1000, 1000000)