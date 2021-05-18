def multiplicacion(x: float, y: float) -> float:
    return x * y

def suma(x: float, y: float) -> float:
    return x + y

def resta(x: float, y: float) -> float:
    return x - y

def division(x: float, y: float) -> float:

    if y == 0:
        return "No se puede dividir por cero."
    return x / y