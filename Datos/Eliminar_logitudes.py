import pandas as pd


df = pd.read_csv('santiago_actualizado_final_REAL_sin_dias_metro.csv')

print(f"Cantidad de filas originales: {df.shape[0]}")

df_filtrado = df[df['longitude'] <= -70.4]

print(f"Cantidad de filas después de eliminar outliers: {df_filtrado.shape[0]}")
print(f"Filas eliminadas: {df.shape[0] - df_filtrado.shape[0]}")


df_filtrado.to_csv('santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud.csv', index=False)

print("\n¡Archivo guardado con éxito como 'datos_sin_outliers_longitud.csv'!")