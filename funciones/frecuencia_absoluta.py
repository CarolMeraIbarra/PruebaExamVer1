# Función para calcular frecuencia absoluta
def frecuencia_absoluta(datos_ordenados, valor_minimo, ancho_clase, numero_intervalos):
    frecuencias = [0] * numero_intervalos
    for dato in datos_ordenados:
        intervalo_index = int((dato - valor_minimo) / ancho_clase)
        if intervalo_index == numero_intervalos:  # Corregir casos donde el dato es el valor máximo
            intervalo_index -= 1
        frecuencias[intervalo_index] += 1
    return frecuencias