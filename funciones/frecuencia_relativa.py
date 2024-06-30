# Función para calcular frecuencia relativa
def frecuencia_relativa(frecuencias):
    total = sum(frecuencias)
    frecuencias_relativas = [(frecuencia / total) * 100 for frecuencia in frecuencias]
    return frecuencias_relativas