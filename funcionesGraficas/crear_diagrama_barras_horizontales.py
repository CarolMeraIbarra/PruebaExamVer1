import matplotlib.pyplot as plt
# Gráfico de barras horizontales
def crear_diagrama_barras_horizontales(categorias, frecuencias):
    plt.figure(figsize=(12, 6))
    plt.barh(categorias, frecuencias,
             height=0.75, edgecolor="k",
             color=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    plt.xlabel("Frecuencias", fontsize=20)
    plt.ylabel("Categorías", fontsize=20)
    plt.title("Diagrama de Barras", fontsize=25)
    plt.grid()
    plt.show()