import pandas as pd

df = pd.read_csv('santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud_metro_corregido.csv')

df_nulos_metro = df[df['fecha_inauguracion_metro'].isnull()]

estaciones_con_nulos = df_nulos_metro['nombre_estacion'].value_counts()

print("=== ESTACIONES CON FECHA DE INAUGURACIÓN NULA ===")
if not estaciones_con_nulos.empty:
    print(estaciones_con_nulos)
    print(f"\nTotal de estaciones distintas con problemas: {len(estaciones_con_nulos)}")
else:
    print("No se encontraron estaciones con valores nulos.")