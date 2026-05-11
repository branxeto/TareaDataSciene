import pandas as pd
import os

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATOS     = os.path.join(BASE_DIR, "..", "Datos")

df = pd.read_csv(os.path.join(DATOS, "BD_Trafico_aereo-2014-2025-1.csv"), sep=None, engine="python", encoding="latin-1")
df.rename(columns={df.columns[0]: "Año"}, inplace=True)

for col in ["OPER_2", "DEST_1_N", "NAC"]:
    df[col] = df[col].astype(str).str.strip().str.upper()

df = df[(df["OPER_2"] == "LLEGAN") & (df["DEST_1_N"] == "SANTIAGO") & (df["PASAJEROS"] > 0)].copy()

pivot = df.pivot_table(index=["Año", "Mes"], columns="NAC", values="PASAJEROS", aggfunc="sum").reset_index()
pivot.columns.name = None
pivot.rename(columns={"INTERNACIONAL": "pax_internacional", "NACIONAL": "pax_nacional"}, inplace=True)
pivot["pax_total"] = pivot["pax_internacional"].fillna(0) + pivot["pax_nacional"].fillna(0)
pivot["key_mes"]   = pivot["Año"].astype(int).astype(str) + "-" + pivot["Mes"].astype(int).astype(str).str.zfill(2)
pivot = pivot.sort_values("key_mes").reset_index(drop=True)
pivot["pax_total_var_pct"] = pivot["pax_total"].pct_change().round(4)
pivot["pax_total_ma3"]     = pivot["pax_total"].rolling(3, min_periods=1).mean().round(0)

airbnb = pd.read_csv(os.path.join(DATOS, "Datos_santigo_final_Junto_con_Datos_IPC.csv"), low_memory=False)
airbnb["archivo_fecha_origen"] = pd.to_datetime(airbnb["archivo_fecha_origen"], errors="coerce")
airbnb["key_mes"] = airbnb["archivo_fecha_origen"].dt.strftime("%Y-%m")

cols = ["key_mes", "pax_internacional", "pax_nacional", "pax_total", "pax_total_var_pct", "pax_total_ma3"]
final = pd.merge(airbnb, pivot[cols], on="key_mes", how="left")
final.drop(columns=["key_mes"], inplace=True)  # ← acá
final.to_csv(os.path.join(DATOS, "santiago_final_con_vuelos.csv"), index=False)

print(f"Listo — {len(final):,} filas, {final.shape[1]} columnas")