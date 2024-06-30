import math
# Función para obtener número de intervalos
def calcular_numero_intervalos(datos):
    n = len(datos)
    numero_intervalos = 1 + 3.3 * math.log10(n)
    return numero_intervalos