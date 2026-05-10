import pandas as pd

def limpiar_csv(archivo_entrada, archivo_salida):
    try:
        df = pd.read_csv(archivo_entrada)
        
        columnas_a_mantener = [
            'id', 
            'neighbourhood', 
            'latitude', 
            'longitude', 
            'room_type', 
            'price', 
            'minimum_nights', 
            'number_of_reviews', 
            'availability_365', 
            'number_of_reviews_ltm', 
            'archivo_fecha_origen'
        ]
        
        df_limpio = df[columnas_a_mantener]
        
        df_limpio.to_csv(archivo_salida, index=False)
        
        print(f"El archivo limpio se guardó como: {archivo_salida}")
        print(f"Columnas finales: {len(df_limpio.columns)} (de las {len(df.columns)} originales)")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de entrada. Revisa el nombre.")
    except KeyError as e:
        print(f"Error: Una de las columnas no existe en el archivo original: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

input_file = 'santiago_historico_limpio.csv'
output_file = 'santiago_historico_finaluwu.csv'

limpiar_csv(input_file, output_file)