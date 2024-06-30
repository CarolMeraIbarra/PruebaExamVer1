# Función para calcular frecuencia acumulada
def frecuencia_acumulada(frecuencias_relativas):
    frecuencias_acumuladas = []
    acumulado = 0
    for frecuencia in frecuencias_relativas:
        acumulado += frecuencia
        frecuencias_acumuladas.append(acumulado)
    return frecuencias_acumuladas