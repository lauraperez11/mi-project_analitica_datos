# Documentación de la Base de Datos

## a) Nombre de la base de datos

Transacciones Bancarias para Detección de Fraude

## b) Fuente (URL)

https://www.kaggle.com/datasets/marusagar/bank-transaction-fraud-detection?resource=download

## c) Descripción general del problema

Esta base de datos contiene información detallada sobre clientes y sus transacciones bancarias, incluyendo datos personales, información de cuentas, características de las transacciones y comportamiento financiero.

El problema principal consiste en identificar transacciones fraudulentas a partir de los patrones observados en los datos.

## d) Objetivo del análisis

Desarrollar un modelo de clasificación que permita detectar transacciones fraudulentas basándose en las características de los clientes y sus transacciones, con el fin de prevenir pérdidas financieras y mejorar la seguridad.

## e) Variable objetivo (variable respuesta)

* **Is_Fraud**

  * Descripción: Indica si la transacción es fraudulenta o no.
  * Tipo: Categórica nominal (binaria: 0 = No fraude, 1 = Fraude).

---

## f) Diccionario de variables

### Variables de identificación

* **Customer_ID**

  * Descripción: Identificador único del cliente.
  * Tipo: Categórica nominal.

* **Customer_Name**

  * Descripción: Nombre del cliente.
  * Tipo: Categórica nominal.

* **Customer_Email**

  * Descripción: Correo electrónico del cliente.
  * Tipo: Categórica nominal.

* **Customer_Contact**

  * Descripción: Número de contacto del cliente.
  * Tipo: Categórica nominal.

* **Transaction_ID**

  * Descripción: Identificador único de la transacción.
  * Tipo: Categórica nominal.

* **Merchant_ID**

  * Descripción: Identificador del comercio.
  * Tipo: Categórica nominal.

---

### Variables demográficas

* **Gender**

  * Descripción: Género del cliente.
  * Tipo: Categórica nominal.

* **Age**

  * Descripción: Edad del cliente.
  * Tipo: Numérica discreta.

* **State**

  * Descripción: Estado o región del cliente.
  * Tipo: Categórica nominal.

* **City**

  * Descripción: Ciudad del cliente.
  * Tipo: Categórica nominal.

---

### Variables de cuenta bancaria

* **Bank_Branch**

  * Descripción: Sucursal bancaria del cliente.
  * Tipo: Categórica nominal.

* **Account_Type**

  * Descripción: Tipo de cuenta (ahorros, corriente, etc.).
  * Tipo: Categórica nominal.

* **Account_Balance**

  * Descripción: Saldo disponible en la cuenta.
  * Tipo: Numérica continua.

---

### Variables de la transacción

* **Transaction_Date**

  * Descripción: Fecha en que se realizó la transacción.
  * Tipo: Categórica ordinal (temporal).

* **Transaction_Time**

  * Descripción: Hora de la transacción.
  * Tipo: Categórica ordinal (temporal).

* **Transaction_Amount**

  * Descripción: Monto de la transacción.
  * Tipo: Numérica continua.

* **Transaction_Type**

  * Descripción: Tipo de transacción (compra, retiro, transferencia, etc.).
  * Tipo: Categórica nominal.

* **Transaction_Currency**

  * Descripción: Moneda utilizada en la transacción.
  * Tipo: Categórica nominal.

* **Transaction_Description**

  * Descripción: Descripción de la transacción.
  * Tipo: Categórica nominal.

---

### Variables del comercio

* **Merchant_Category**

  * Descripción: Categoría del comercio (retail, comida, etc.).
  * Tipo: Categórica nominal.

---

### Variables tecnológicas y de comportamiento

* **Transaction_Device**

  * Descripción: Dispositivo usado para la transacción.
  * Tipo: Categórica nominal.

* **Device_Type**

  * Descripción: Tipo de dispositivo (móvil, computador, etc.).
  * Tipo: Categórica nominal.

* **Transaction_Location**

  * Descripción: Ubicación donde se realizó la transacción.
  * Tipo: Categórica nominal.

---

## g) Número de observaciones

200,000 registros

## h) Número de variables

24 variables

---

## i) Posibles hipótesis de estudio

1. Las transacciones realizadas desde dispositivos inusuales tienen mayor probabilidad de ser fraudulentas.
2. Los montos de transacción más altos están asociados con una mayor probabilidad de fraude.
3. Las transacciones en ubicaciones diferentes a la residencia del cliente presentan mayor riesgo de fraude.
4. Ciertas categorías de comercio están más asociadas con transacciones fraudulentas.
5. El comportamiento temporal (hora del día) influye en la probabilidad de fraude.
