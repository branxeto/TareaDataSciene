import pandas as pd
from scipy.spatial import KDTree

def unir_estaciones_metro(archivo_santiago, archivo_metro, archivo_salida):
    try:
        print("Cargando archivos...")
        df_santiago = pd.read_csv(archivo_santiago)
        df_metro = pd.read_csv(archivo_metro)

        coords_metro = df_metro[['lat', 'lon']].values
        
        arbol_metro = KDTree(coords_metro)

        coords_propiedades = df_santiago[['latitude', 'longitude']].values

        distancias, indices = arbol_metro.query(coords_propiedades)

        df_santiago['nombre_estacion'] = df_metro.iloc[indices]['nombre_estacion'].values
        df_santiago['fecha_inauguracion_metro'] = df_metro.iloc[indices]['fecha_inauguracion'].values
        
        df_santiago.to_csv(archivo_salida, index=False)

        print(f"--- Proceso exitoso ---")
        print(f"Archivo generado: {archivo_salida}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

archivo_principal = 'santiago_dolar_aproximado.csv'
archivo_estaciones = 'estaciones_metro_santiago.csv'
resultado_final = 'santiago_final_con_metro.csv'

unir_estaciones_metro(archivo_principal, archivo_estaciones, resultado_final)