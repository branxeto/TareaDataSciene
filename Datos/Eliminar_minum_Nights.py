import pandas as pd


df = pd.read_csv("santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud_metro_corregido.csv")


df["minimum_nights"] = pd.to_numeric(df["minimum_nights"], errors="coerce")

df_filtrado = df[df["minimum_nights"] <= 7]


df_filtrado.to_csv("santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud_metro_corregido_Eliminadas_min_nights.csv", index=False)


filas_eliminadas = len(df) - len(df_filtrado)
print(f"datos limpiados")
print(f"Filas originales: {len(df)}")
print(f"Filas eliminadas (mayores a 7 días): {filas_eliminadas}")
print(f"Filas resultantes en el nuevo archivo: {len(df_filtrado)}")