import sqlite3
import pandas as pd

conn = sqlite3.connect('database/dataset_clasificacion.db')

# 1. Conteo del número de transacciones 
print(pd.read_sql("""
SELECT COUNT(*) AS TOTAL_TRANSACCIONES 
FROM dataset_clasificacion
""", conn))

# 2. Promedio de monto de transacción
print(pd.read_sql("""
SELECT AVG(Transaction_Amount) AS PROMEDIO_MONTO FROM dataset_clasificacion
""", conn))

# 3. Fraudes vs no fraudes
print(pd.read_sql("""
SELECT Is_Fraud, 
COUNT(*) as CANTIDAD
FROM dataset_clasificacion
GROUP BY Is_Fraud
""", conn))

# 4. Promedio por tipo de transacción
print(pd.read_sql("""
SELECT Transaction_Type, 
AVG(Transaction_Amount) as PROMEDIO_TIPO_DE_TRANSACCION
FROM dataset_clasificacion
GROUP BY Transaction_Type
""", conn))

# 5. Transacciones sospechosas (altos montos)
print(pd.read_sql("""
SELECT Customer_Name, Transaction_Amount
FROM dataset_clasificacion
WHERE Transaction_Amount > 50000
LIMIT 20
""", conn))


conn.close()