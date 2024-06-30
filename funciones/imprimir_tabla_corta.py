# Función para imprimir la tabla
def imprimir_tabla_corta(categorias, frecuencias, frecuencias_relativas, frecuencias_acumuladas):
    print(f'{"Categoría":<15}{"Frecuencia absoluta":<20}{"Frecuencia relativa (%)":<25}{"Frecuencia acumulada (%)":<25}')
    print(f'{"----------":<15}{"------------------":<20}{"----------------------":<25}{"------------------------":<25}')

    for i in range(len(categorias)):
        print(f'{categorias[i]:<15}{frecuencias[i]:<20}{frecuencias_relativas[i]:<25.2f}{frecuencias_acumuladas[i]:<25.2f}')
