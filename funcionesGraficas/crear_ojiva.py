import matplotlib.pyplot as plt
# Ojiva
def crear_ojiva(marcas_clase, frecuencias_acumuladas):
    datos_x = [0] + marcas_clase
    datos_y = [0] + frecuencias_acumuladas 

    plt.figure(figsize=(12, 6))

    plt.plot(datos_x, datos_y, 
             linewidth=2, color="r", linestyle=":", 
             marker="v", markersize=5, markerfacecolor="y", markeredgecolor="b")

    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencia acumulada (%)", fontsize=20)
    plt.title("Ojiva", fontsize=25)
    plt.xticks(marcas_clase)  # Añadir límites superiores en el eje x
    plt.grid(True)
    plt.show()