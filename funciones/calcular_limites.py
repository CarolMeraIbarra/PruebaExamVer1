# Función para determinar los límites de cada clase
def calcular_limites(valor_minimo, ancho_clase, numero_intervalos):
    limites_inferiores = [valor_minimo + i * ancho_clase for i in range(numero_intervalos)]
    limites_superiores = [valor_minimo + (i + 1) * ancho_clase for i in range(numero_intervalos)]
    return limites_inferiores, limites_superiores