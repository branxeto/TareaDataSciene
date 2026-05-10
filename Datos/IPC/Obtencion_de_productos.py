import pandas as pd

# Leer el archivo CSV
df = pd.read_csv(
    "Base anonimizada IPC 2023.csv",
    sep="\\",
    encoding="latin1"
)
# Extraer solo la columna glosa_producto
# eliminar nulos y duplicados
glosas_unicas = (
    df["Glosa_Producto"]
    .dropna()
    .drop_duplicates()
)

# Guardar en un nuevo CSV
glosas_unicas.to_csv("glosa_productos_unicos.csv", index=False)

print("CSV generado correctamente.")