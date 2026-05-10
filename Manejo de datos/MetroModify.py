import json
import pandas as pd

def transformar_json_archivo_a_csv(archivo_entrada, archivo_salida='estaciones_metro_santiago.csv'):
    try:
        # 1. Cargar el archivo JSON local
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lista_estaciones = []
        
        # 2. Iterar sobre los elementos del JSON
        for element in data.get('elements', []):
            if element.get('type') == 'node':
                # Extraemos datos básicos
                info = {
                    'id_osm': element.get('id'),
                    'lat': element.get('lat'),
                    'lon': element.get('lon')
                }
                
                # Extraemos los tags (metadatos)
                tags = element.get('tags', {})
                info['nombre_estacion'] = tags.get('name')
                info['accesibilidad'] = tags.get('wheelchair')
                info['fecha_inauguracion'] = tags.get('start_date')
                
                lista_estaciones.append(info)
        
        # 3. Crear el DataFrame y guardar
        df = pd.DataFrame(lista_estaciones)
        
        # Limpieza rápida: eliminar estaciones sin nombre si las hay
        df = df.dropna(subset=['nombre_estacion'])
        
        df.to_csv(archivo_salida, index=False, encoding='utf-8')
        
        print(f"Proceso exitoso:")
        print(f"- Archivo procesado: {archivo_entrada}")
        print(f"- Archivo creado: {archivo_salida}")
        print(f"- Total de estaciones encontradas: {len(df)}")
        
        return df

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_entrada}' no tiene un formato JSON válido")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Ejecución ---
# Cambia 'estaciones.json' por el nombre de tu archivo
df_metro = transformar_json_archivo_a_csv('Metros.JSON')

# Ver los primeros resultados
if df_metro is not None:
    print("\nVista previa de los datos:")
    print(df_metro[['nombre_estacion', 'lat', 'lon']].head())