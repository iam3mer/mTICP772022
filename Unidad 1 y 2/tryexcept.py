def division(x: float, y:float)->float:

    try:
        return x / y
        #return z
    except NameError:
        print("Valor no declarado")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Cualquier otra cosa")

print(division(36,-3))