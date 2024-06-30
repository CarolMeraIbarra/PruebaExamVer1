# Función para calcular la marca de clase
def calcular_marcas_clase(limites_inferiores, limites_superiores):
    marcas_clase = [(limite_inferior + limite_superior) / 2 for limite_inferior, limite_superior in zip(limites_inferiores, limites_superiores)]
    return marcas_clase