import pandas as pd


df = pd.read_csv('santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud.csv')


estaciones_linea6 = [
    'Inés de Suárez', 
    'Chile España', 
    'Presidente Pedro Aguirre Cerda', 
    'Bío Bío', 
    'Cerrillos', 
    'Lo Valledor'
]


filtro_estaciones = df['nombre_estacion'].isin(estaciones_linea6)
df.loc[filtro_estaciones, 'fecha_inauguracion_metro'] = '2017-11-02'


nulos_restantes = df['fecha_inauguracion_metro'].isnull().sum()
print(f"Nulos restantes en 'fecha_inauguracion_metro': {nulos_restantes}")

df.to_csv('santiago_actualizado_final_REAL_sin_dias_metro_sin_outliers_longitud_metro_corregido.csv', index=False)
print("¡Fechas corregidas y archivo guardado como 'datos_metro_corregido.csv'!")