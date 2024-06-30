# Función para calcular la frecuencia absoluta
def frecuencia_absoluta_c(datos_ordenados):
    categorias = []
    frecuencias = []
    for dato in datos_ordenados:
        if dato in categorias:
            index = categorias.index(dato)
            frecuencias[index] += 1
        else:
            categorias.append(dato)
            frecuencias.append(1)
    return categorias, frecuencias