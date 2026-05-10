import pandas as pd

def fusionar_dolar_proximidad(archivo_principal, archivo_dolar, archivo_salida):
    try:
        print("Cargando y preparando datos...")
        df_principal = pd.read_csv(archivo_principal)
        df_dolar = pd.read_csv(archivo_dolar)

        df_principal['archivo_fecha_origen'] = pd.to_datetime(df_principal['archivo_fecha_origen'])
        df_dolar['Fecha'] = pd.to_datetime(df_dolar['Fecha'], dayfirst=True)

        df_principal = df_principal.sort_values('archivo_fecha_origen')
        df_dolar = df_dolar.sort_values('Fecha')

        df_final = pd.merge_asof(
            df_principal,
            df_dolar,
            left_on='archivo_fecha_origen',
            right_on='Fecha',
            direction='nearest' 
        )

        df_final = df_final.drop(columns=['Fecha'])
        df_final['archivo_fecha_origen'] = df_final['archivo_fecha_origen'].dt.strftime('%Y-%m-%d')

        df_final.to_csv(archivo_salida, index=False)
        
        print(f"Fusión completada usando la fecha más cercana.")
        print(f"Archivo guardado como: {archivo_salida}")

    except Exception as e:
        print(f"Error: {e}")

archivo_grande = 'santiago_historico_finaluwu.csv'
archivo_precios_dolar = 'DOLAR_OBS_ADO - Hoja 1.csv'
archivo_resultado = 'santiago_dolar_aproximado.csv'

fusionar_dolar_proximidad(archivo_grande, archivo_precios_dolar, archivo_resultado)