# Función para determinar el ancho de cada clase
def calcular_ancho_clase(rango, numero_intervalos):
    intervalo_redondeado = round(numero_intervalos)
    ancho_clase = rango / intervalo_redondeado
    return ancho_clase, intervalo_redondeado