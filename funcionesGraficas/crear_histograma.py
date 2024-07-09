import matplotlib.pyplot as plt
# Histograma
def crear_histograma(marcas_clase, frecuencias, ancho_clase):
    plt.figure(figsize=(12, 6))
    plt.bar(marcas_clase, frecuencias, width=ancho_clase, edgecolor="k", color=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.xticks(marcas_clase)  # Añadir marcas de clase en el eje x
    plt.show()