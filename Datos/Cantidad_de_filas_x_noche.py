import pandas as pd

df = pd.read_csv("santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud_metro_corregido_Eliminadas_min_nights.csv")

df["minimum_nights"] = pd.to_numeric(df["minimum_nights"], errors="coerce")
df_conteo = df.dropna(subset=["minimum_nights"])

distribucion_dias = df_conteo["minimum_nights"].value_counts().sort_index()

tabla_dias = distribucion_dias.reset_index()
tabla_dias.columns = [
    "Cantidad de Dias minimos",
    "Cantidad de Propiedades",
]

print("Dias minimos x propiedad")
print(tabla_dias.to_string(index=False))
