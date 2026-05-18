import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# 1. CARGAR Y PROCESAR EL DATASET (Pasos anteriores)
# ==============================================================================
# Cargar tu archivo
df = pd.read_csv("dataset_airbnb_procesado.csv")

variables_con_log = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "number_of_reviews_ltm",
]


print("\n--- GENERANDO Y GUARDANDO GRÁFICOS DE VARIABLES LOGARÍTMICAS ---")

# Bucle exclusivo para las variables de tu lista
for columna in variables_con_log:
    # Crear la figura del gráfico
    plt.figure(figsize=(8, 4))

    # Dibujar el histograma con su curva de densidad (KDE)
    sns.histplot(df[columna], kde=True, color="skyblue")

    # Configurar títulos y etiquetas
    plt.title(f"Distribución de {columna} (Escala Logarítmica)")
    plt.xlabel(f"{columna} (log)")
    plt.ylabel("Frecuencia")

    # Ajustar diseño para que no se corten los textos
    plt.tight_layout()

    # GUARDAR LA GRÁFICA: Se guardará como 'grafico_price.png', 'grafico_minimum_nights.png', etc.
    nombre_grafico = f"grafico_{columna}.png"
    plt.savefig(nombre_grafico, dpi=300)

    # Mostrar en pantalla el reporte estadístico de esa variable
    print(f"📊 Gráfico guardado como: {nombre_grafico}")
    print(f"{columna} - skewness (Asimetría) > {df[columna].skew():.2f}")
    print(f"{columna} - Kurtosis (Curtosis)  > {df[columna].kurt():.2f}")
    print("-" * 50)

    # Cerrar la figura para liberar memoria de la computadora
    plt.close()

print("\n🎉 ¡Todo listo! Las 4 imágenes quedaron guardadas en tu carpeta.")