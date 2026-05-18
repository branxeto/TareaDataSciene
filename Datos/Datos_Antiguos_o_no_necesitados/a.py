
import pandas as pd
import re
from glob import glob

mapeo_raw = {
    "SERVICIO DE ALOJAMIENTO TURÍSTICO ": "alojamiento",
    "SERVICIO DE ALOJAMIENTO TURÍSTICO" : "alojamiento",
    "SERVICIOS DE ALOJAMIENTO": "alojamiento",
    "ALMUERZO Y CENAS CONSUMIDO FUERA DEL HOGAR": "comida_fuera",
    "ALMUERZO  Y CENAS CONSUMIDO FUERA DEL HOGAR": "comida_fuera",
    "ALIMENTOS CONSUMIDOS FUERA DEL HOGAR": "comida_fuera",
    "ALIMENTOS ADQUIRIDOS EN RESTAURANTES, CAFÉS Y SIMILARES": "comida_fuera",
    "GAS LICUADO": "gas_licuado",
    "PARAFINA": "parafina",
    "SERVICIO DE TRANSPORTE EN TAXI": "taxi",
    "SERVICIO DE TRANSPORTE EN TAXI ": "taxi",
    "TRANSPORTE PRIVADO DE PASAJEROS": "taxi",
    "SERVICIOS PARA LA CONSERVACIÓN Y REPARACIÓN DE LA VIVIENDA": "mantencion_hogar",
    "SERVICIOS PARA EL MANTENIMIENTO DE LA VIVIENDA": "mantencion_hogar",
}

meses = {
    "Enero": "01",
    "Febrero": "02",
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05",
    "Junio": "06",
    "Julio": "07",
    "Agosto": "08",
    "Septiembre": "09",
    "Octubre": "10",
    "Noviembre": "11",
    "Diciembre": "12",
}


resultados = []

archivos = glob("IPC_*.csv")

for archivo in archivos:
    print(f"Procesando: {archivo}")

    df = pd.read_csv(archivo)

    # Buscar columna correcta
    columna_glosa = None

    for col in df.columns:
        if col.lower() == "glosa_producto":
            columna_glosa = col
            break

    if columna_glosa is None:
        print(f"No se encontró Glosa_Producto en {archivo}")
        continue

    # Filtrar solo productos del mapeo
    df = df[df[columna_glosa].isin(mapeo_raw.keys())]

    # Buscar columnas de precios mensuales
    columnas_pm = [
        c for c in df.columns
        if re.match(r'(?i)^pm_?[A-Za-z]+\d{4}$', c)
    ]

    for _, fila in df.iterrows():

        categoria = mapeo_raw[fila[columna_glosa]]

        for col in columnas_pm:

            match = re.search(r'([A-Za-z]+)(\d{4})$', col)

            if not match:
                continue

            mes_texto = match.group(1).capitalize()
            anio = match.group(2)

            if mes_texto not in meses:
                continue

            fecha = f"{anio}-{meses[mes_texto]}-01"

            valor = fila[col]

            # Limpiar valores string tipo 12345,67
            if isinstance(valor, str):
                valor = valor.replace('.', '')
                valor = valor.replace(',', '.')

            valor = pd.to_numeric(valor, errors='coerce')

            if pd.isna(valor):
                continue

            resultados.append({
                "FECHA": fecha,
                "CONCEPTO": categoria,
                "PRECIO": valor
            })


df_final = pd.DataFrame(resultados)

df_final = (
    df_final
    .groupby(["FECHA", "CONCEPTO"], as_index=False)["PRECIO"]
    .mean()
)

# Renombrar columna
df_final.rename(columns={"PRECIO": "PRECIO_PROMEDIO"}, inplace=True)

# Ordenar
df_final = df_final.sort_values(["FECHA", "CONCEPTO"])

# Guardar CSV final
df_final.to_csv("ipc_unificado.csv", index=False)

print("CSV generado: ipc_unificado.csv")
print(df_final.head())

