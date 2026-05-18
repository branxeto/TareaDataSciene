import pandas as pd


df = pd.read_csv('santiago_actualizado_final_REAL.csv')


df = df.drop('antiguedad_metro_dias', axis=1)


df.to_csv('santiago_actualizado_final_REAL_sin_dias_metro.csv', index=False)

print("¡Columna eliminada con éxito y archivo guardado!")