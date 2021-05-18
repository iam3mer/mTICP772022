def fibonacci(n:int=50)->int:
    n1, n2 = 0, 1
    while n2 < n:
        print(n2)
        n1, n2 = n2, n1 + n2

fibonacci()