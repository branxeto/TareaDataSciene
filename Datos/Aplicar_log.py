import numpy as np
import pandas as pd


df = pd.read_csv("dataset_sin_precios_cero.csv")


columnas_criticas = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "number_of_reviews_ltm",
]

for col in columnas_criticas:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)


for col in columnas_criticas:
    df[col] = np.log1p(df[col])

df_filtrado = df[df["price"] <= 15].copy()


df_filtrado[columnas_criticas] = df_filtrado[columnas_criticas].round(4)


df_filtrado.to_csv(
    "dataset_airbnb_procesado.csv", sep=",", encoding="utf-8-sig", index=False
)

print( "Listo.")