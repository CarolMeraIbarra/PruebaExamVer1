import matplotlib.pyplot as plt
# Gráfico de pastel
def crear_grafico_pastel(categorias, frecuencias_relativas):
    plt.figure(figsize=(8, 8))
    plt.pie(frecuencias_relativas, 
            labels=categorias, 
            autopct="%0.1f%%", 
            pctdistance=0.8, 
            startangle=90, 
            counterclock=False, 
            colors=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    plt.title("Gráfico de pastel", fontsize=20)
    plt.show()