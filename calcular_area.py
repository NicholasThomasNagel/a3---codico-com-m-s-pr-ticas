
import math

def calcular_area(tipo, a, b=0):
    if tipo == 'quadrado':
        return a * a
    elif tipo == 'retangulo':
        return a * b
    elif tipo == 'circulo':
        return math.pi * a * a
    else:
        return None

print(calcular_area('quadrado', 4))
print(calcular_area('retangulo', 4, 5))
print(calcular_area('circulo', 3))
print(calcular_area('triangulo', 4, 5))
