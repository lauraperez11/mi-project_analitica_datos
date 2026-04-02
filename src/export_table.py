
# ===================================================================== #
# Librerías necesarias para la extracción, transformación y carga (ETL) #
# ===================================================================== #

import pandas as pd
import sqlite3
from pathlib import Path

# =============================================================================================== #
# Definir rutas de archivos y base de datos usando pathlib para mayor flexibilidad y portabilidad #
# =============================================================================================== #

BASE_DIR = Path(__file__).resolve().parents[1]

csv_path = BASE_DIR / "data/raw/dataset_regresion.csv"
db_path = BASE_DIR / "database/dataset_regresion.db"

# ======================================================================================= #
# Cargar datos en la base de datos SQLite y Leer CSV donde es importante el separador ";" #
# ======================================================================================= #

df = pd.read_csv(csv_path, sep=",")

conn = sqlite3.connect(db_path)

# ============================================================================================================== #
# Cargar el DataFrame en la tabla "dataset_regresion" de la base de datos SQLite, reemplazando la tabla si ya existe #
# ============================================================================================================== #

df.to_sql("dataset_regresion", conn, if_exists="replace", index=False)

conn.close()

print("¡Tabla dataset_regresion Creada Correctamente!")