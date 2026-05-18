import numpy as np
import pandas as pd

# 1. Cargar tu archivo CSV original
df = pd.read_csv("dataset_airbnb_procesado.csv")

print("=" * 60)
print(f"   AUDITORÍA COMPLETA DE CASILLAS (Total Filas: {len(df)})")
print("=" * 60)

# Creamos una lista para armar una tabla resumen al final
resumen_datos = []

for col in df.columns:
    # 1. Contar valores Nulos/Vacíos (aplica para cualquier tipo de columna)
    total_nulls = df[col].isna().sum()
    pct_nulls = (total_nulls / len(df)) * 100

    # 2. Contar Ceros (solo si la columna es numérica o se puede convertir a número)
    col_numerica = pd.to_numeric(df[col], errors="coerce")
    total_zeros = (col_numerica == 0).sum()
    pct_zeros = (total_zeros / len(df)) * 100

    # Guardar los resultados de esta columna
    resumen_datos.append(
        {
            "Columna": col,
            "Tipo de Dato": str(df[col].dtype),
            "Vacíos (Qty)": total_nulls,
            "Vacíos (%)": f"{pct_nulls:.2f}%",
            "Ceros (Qty)": total_zeros,
            "Ceros (%)": f"{pct_zeros:.2f}%",
        }
    )

# 3. Convertir el resumen en un nuevo DataFrame para mostrarlo como una tabla limpia
df_reporte = pd.DataFrame(resumen_datos)

# Mostrar la tabla completa en pantalla
print(df_reporte.to_string(index=False))
print("=" * 60)

# OPCIONAL: Si quieres guardar este reporte en un Excel para revisarlo con calma:
# df_reporte.to_csv("reporte_auditoria_columnas.csv", sep=";", index=False)