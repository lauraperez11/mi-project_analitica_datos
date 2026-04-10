import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.impute import KNNImputer
from scipy.stats import chi2_contingency, kruskal, f_oneway

# ------------------------
# CONFIG
# ------------------------
st.set_page_config(page_title="Fraud Data Science Lab", layout="wide", page_icon="💳")

st.title("🛡️ Sistema de Análisis de Fraude Transaccional")

# ------------------------
# LOAD DATA (ROBUSTO)
# ------------------------
@st.cache_data
def load_data():
    try:
        # Ruta absoluta basada en ubicación del script
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_path, "data", "raw", "dataset_clasificacion.csv")

        df = pd.read_csv(file_path)
        return df

    except Exception as e:
        st.error(f"Error cargando archivo: {e}")
        st.write("Ruta usada:", file_path)
        return pd.DataFrame()

df = load_data()

# ------------------------
# SI NO CARGA
# ------------------------
if df.empty:
    st.warning("❌ No se pudo cargar el dataset. Verifica que esté en la carpeta /data/raw y que el nombre sea correcto.")
    st.stop()

# ------------------------
# SIDEBAR
# ------------------------
menu = st.sidebar.radio(
    "Navegación",
    ["📊 EDA", "🧠 Imputación", "🔗 Correlación", "🧪 Pruebas"]
)

# ========================
# 📊 EDA
# ========================
if menu == "📊 EDA":
    st.header("Análisis Exploratorio")

    col1, col2, col3 = st.columns(3)
    col1.metric("Registros", f"{df.shape[0]:,}")
    col2.metric("Fraudes", f"{df['Is_Fraud'].sum():,}")
    col3.metric("% Fraude", f"{df['Is_Fraud'].mean()*100:.2f}%")

    st.dataframe(df.head())

    var = st.selectbox("Variable", ['Transaction_Amount','Age','Account_Balance'])

    fig, ax = plt.subplots()
    sns.histplot(df, x=var, hue="Is_Fraud", kde=True, ax=ax)
    st.pyplot(fig)

# ========================
# 🧠 IMPUTACIÓN
# ========================
elif menu == "🧠 Imputación":
    st.header("Imputación de datos")

    num_cols = df.select_dtypes(include=['number']).columns

    metodo = st.selectbox("Método", ["Media", "KNN"])

    df_missing = df.copy()

    if st.checkbox("Simular missing (20%)"):
        mask = np.random.rand(*df[num_cols].shape) < 0.2
        df_missing[num_cols] = df_missing[num_cols].mask(mask)

    if metodo == "Media":
        df_imputed = df_missing.copy()
        df_imputed[num_cols] = df_missing[num_cols].fillna(df_missing[num_cols].mean())
    else:
        imputer = KNNImputer(n_neighbors=3)
        df_imputed = df_missing.copy()
        df_imputed[num_cols] = imputer.fit_transform(df_missing[num_cols])

    fig, ax = plt.subplots()
    sns.kdeplot(df['Transaction_Amount'], label="Original", ax=ax)
    sns.kdeplot(df_imputed['Transaction_Amount'], label=metodo, ax=ax)
    ax.legend()
    st.pyplot(fig)

# ========================
# 🔗 CORRELACIÓN
# ========================
elif menu == "🔗 Correlación":
    st.header("Correlación")

    metodo = st.selectbox("Método", ["pearson","spearman","kendall"])

    num_cols = df.select_dtypes(include=['number']).columns.drop('Is_Fraud')

    corr = df[num_cols].corr(method=metodo)

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# ========================
# 🧪 PRUEBAS
# ========================
elif menu == "🧪 Pruebas":
    st.header("Pruebas estadísticas")

    tipo = st.selectbox("Tipo", ["Numérica", "Categórica"])

    if tipo == "Numérica":
        var = st.selectbox("Variable", ["Transaction_Amount","Age","Account_Balance"])

        g0 = df[df['Is_Fraud']==0][var]
        g1 = df[df['Is_Fraud']==1][var]

        metodo = st.radio("Método", ["ANOVA","Kruskal"])

        if metodo == "ANOVA":
            stat, p = f_oneway(g0,g1)
        else:
            stat, p = kruskal(g0,g1)

        st.write("p-value:", p)

        fig, ax = plt.subplots()
        sns.boxplot(x='Is_Fraud', y=var, data=df, ax=ax)
        st.pyplot(fig)

    else:
        cat_cols = df.select_dtypes(include='object').columns
        var = st.selectbox("Variable", cat_cols)

        tabla = pd.crosstab(df[var], df['Is_Fraud'])
        chi2, p, dof, ex = chi2_contingency(tabla)

        st.write("p-value:", p)

        st.dataframe(tabla)

        fig, ax = plt.subplots()
        tabla_pct = tabla.div(tabla.sum(1), axis=0)
        tabla_pct.plot(kind='bar', stacked=True, ax=ax)
        st.pyplot(fig)