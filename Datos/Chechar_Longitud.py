import pandas as pd


df = pd.read_csv('santiago_actualizado_final_REAL_sin_dias_metro.csv')

cantidad_outliers = (df['longitude'] > -70.4).sum()


porcentaje_outliers = (cantidad_outliers / len(df)) * 100

print(f"Cantidad de registros con longitud > -70.4: {cantidad_outliers}")
print(f"Representan el {porcentaje_outliers:.2f}% del total de los datos.")
