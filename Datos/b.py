import pandas as pd

# 1. Cargar tu archivo CSV
df = pd.read_csv("santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud_metro_corregido_Eliminadas_min_nights.csv")

# 2. Asegurar que la columna 'price' sea numérica
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# 3. ELIMINAR REALMENTE LOS NULOS Y LOS CEROS
# Guardamos solo las filas donde el precio NO sea nulo y además sea MAYOR a 0
df_limpio = df[df["price"].notna() & (df["price"] > 0)]

# 4. Guardar el archivo limpio resultante
df_limpio.to_csv("dataset_sin_precios_cero.csv", index=False)

# 5. Reporte en pantalla
filas_borradas = len(df) - len(df_limpio)
print(f"✅ ¡Limpieza de precios completada!")
print(f"Filas iniciales: {len(df)}")
print(f"Filas eliminadas (valores nulos o iguales a $0): {filas_borradas}")
print(f"Filas finales guardadas: {len(df_limpio)}")