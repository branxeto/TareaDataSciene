import pandas as pd

# Configuración de archivos
ENTRADA = 'santiago_historico_total.csv'
SALIDA = 'santiago_historico_limpio.csv'

def limpiar_dataset_por_review():
    try:
        print(f"Leyendo archivo: {ENTRADA}...")
        
        # Leemos el CSV. Usamos low_memory=False por si el archivo es muy grande
        df = pd.read_csv(ENTRADA, low_memory=False)
        
        filas_iniciales = len(df)
        print(f"Registros totales antes de limpiar: {filas_iniciales}")

        # 1. Eliminamos las filas donde 'last_review' es NaN (nulo)
        # subset indica qué columna mirar para decidir la eliminación
        df_limpio = df.dropna(subset=['last_review'])
        
        # 2. (Opcional) Aseguramos que la columna sea de tipo datetime para futuros análisis
        df_limpio['last_review'] = pd.to_datetime(df_limpio['last_review'], errors='coerce')
        
        # Eliminamos si alguna conversión a fecha falló (opcional pero recomendado)
        df_limpio = df_limpio.dropna(subset=['last_review'])

        filas_finales = len(df_limpio)
        eliminadas = filas_iniciales - filas_finales

        print(f"Registros eliminados (sin review): {eliminadas}")
        print(f"Registros restantes: {filas_finales}")

        # 3. Guardamos el resultado
        df_limpio.to_csv(SALIDA, index=False, encoding='utf-8')
        print(f"Archivo guardado exitosamente en: {SALIDA}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ENTRADA}. Asegúrate de haber terminado la descarga.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar la limpieza
limpiar_dataset_por_review()