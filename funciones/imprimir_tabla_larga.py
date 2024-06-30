# Función para imprimir la tabla
def imprimir_tabla_larga(numero_intervalos, limites_inferiores, limites_superiores, marcas_clase, frecuencias, frecuencias_relativas, frecuencias_acumuladas):
    print(f'{"Clase":<10}{"Límites inferiores":<20}{"Límites superiores":<20}{"Marca de clase":<20}{"f_a":<10}{"f_r (%)":<10}{"F acumulada (%)":<20}')
    print(f'{"-----":<10}{"------------------":<20}{"------------------":<20}{"----------------":<20}{"---":<10}{"-------":<10}{"------------------":<20}')

    for i in range(numero_intervalos):
        print(f'{i+1:<10}{limites_inferiores[i]:<20.2f}{limites_superiores[i]:<20.2f}{marcas_clase[i]:<20.3f}{frecuencias[i]:<10}{frecuencias_relativas[i]:<10.2f}{frecuencias_acumuladas[i]:<20.2f}')
