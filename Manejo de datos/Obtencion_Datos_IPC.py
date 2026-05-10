import pandas as pd

# Configuración de archivos
ENTRADA = "Datos/IPC/Base anonimizada IPC 2023.csv"
SALIDA = 'IPC_2023.csv'

glosas_objetivo = [
    "SERVICIOS DE ALOJAMIENTO",
    "SERVICIOS PARA EL MANTENIMIENTO DE LA VIVIENDA",
    "GAS LICUADO",
    "PARAFINA",
    "OTROS COMBUSTIBLES DE USO DOMÉSTICO",
    "ARTÍCULOS PARA CALEFACCIÓN DEL HOGAR",
    "SERVICIOS DE ESTACIONAMIENTO",
    "ALIMENTOS ADQUIRIDOS EN RESTAURANTES, CAFÉS Y SIMILARES",
    "BEBIDAS NO ALCOHÓLICAS ADQUIRIDAS EN RESTAURANTES, CAFÉS Y SIMILARES",
    "BEBIDAS ALCOHÓLICAS ADQUIRIDAS EN RESTAURANTES, CAFÉS Y SIMILARES",
    "TRANSPORTE PRIVADO DE PASAJEROS",
    "TRANSPORTE EN TAXI COLECTIVO",
    "TRANSPORTE EN MICROBUS",
    "SERVICIOS DE ALARMA PARA LA VIVIENDA",
    "CAMAS",
    "COLCHONES",
    "MUEBLES PARA LIVING",
    "TEXTILES PARA CAMA",
    "REFRIGERADORES",
    "LAVADORAS",
    "COCINAS",

]



def limpiar_dataset_del_IPC():
    try:
        print("Leyendo archivo")

        df = pd.read_csv(
            ENTRADA,
            sep="\\",
            encoding="latin1",
            low_memory=False
        )

        print("Columnas del dataset:")
        print(df.columns)

        filas_iniciales = len(df)

        #Filtro Para Obtener solo las solicitadas

        df_filtrado = df[df["Glosa_Producto"].isin(glosas_objetivo)]

        filas_finales = len(df_filtrado)

        print(f"Filas originales: {filas_iniciales}")
        print(f"Filas filtradas: {filas_finales}")

        # Guardar resultado
        df_filtrado.to_csv(SALIDA, index=False, encoding="utf-8")
        print("Archivo guardado")

    except Exception as e:
        print("Error:", e)

limpiar_dataset_del_IPC()