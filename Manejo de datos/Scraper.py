import requests
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO
import os
import time

# Tus headers de Firefox/Ubuntu
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0',
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Origin': 'https://insideairbnb.com',
    'Referer': 'https://insideairbnb.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Sites': 'same-site'
}

CSV_FINAL = 'santiago_historico_total.csv'

def ejecutar_proceso_historico(años=10):
    print(f"Iniciando consolidación...")
    fecha_actual = datetime.now()
    fecha_limite = fecha_actual - timedelta(days=años * 365)
    archivos_encontrados = 0
    fecha_temp = fecha_actual

    if os.path.exists(CSV_FINAL):
        os.remove(CSV_FINAL)

    while fecha_temp > fecha_limite:
        fecha_str = fecha_temp.strftime('%Y-%m-%d')
        url = f"https://data.insideairbnb.com/chile/rm/santiago/{fecha_str}/visualisations/listings.csv.gz"
        
        try:
            check = requests.head(url, headers=HEADERS, timeout=5)
            if check.status_code == 200:
                res = requests.get(url, headers=HEADERS)
                content = BytesIO(res.content)
                
                # INTENTO 1: Leer como GZIP (estándar)
                try:
                    df_temp = pd.read_csv(content, compression='gzip')
                except Exception:
                    # INTENTO 2: Si falla, leer como CSV normal (el error b'id' indica texto plano)
                    content.seek(0) # Volvemos al inicio del buffer
                    df_temp = pd.read_csv(content)
                
                df_temp['archivo_fecha_origen'] = fecha_str
                
                # Escritura incremental
                modo = 'w' if not os.path.exists(CSV_FINAL) else 'a'
                header = True if modo == 'w' else False
                df_temp.to_csv(CSV_FINAL, mode=modo, index=False, header=header, encoding='utf-8')
                
                archivos_encontrados += 1
                if archivos_encontrados % 5 == 0:
                    print(f"HITO: {archivos_encontrados} archivos en '{CSV_FINAL}'")
                
                fecha_temp -= timedelta(days=15)
            else:
                fecha_temp -= timedelta(days=1)
        except Exception as e:
            print(f"Error en {fecha_str}: {e}")
            fecha_temp -= timedelta(days=1)

    print(f"Completado. Total: {archivos_encontrados}")

ejecutar_proceso_historico(10)