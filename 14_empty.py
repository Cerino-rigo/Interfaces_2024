import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.ticker import MultipleLocator

# Configuración de página
st.set_page_config(page_title="Análisis de Variables vs Tiempo",
                   page_icon="⏱️",
                   layout="wide", # Forma de layout ancho o compacto (centered)
                   initial_sidebar_state="collapsed" # Definimos si el sidebar aparece expandido (expanded) o colapsado
)
st.title("Comparación de Variables vs Tiempo")

# Crear un espacio reservado con st.empty()
placeholder = st.empty()

# Botón en el sidebar para actualizar el contenido del espacio reservado
if st.sidebar.button("Actualizar Contenido"):
    with placeholder:
        st.write("Actualizando contenido...")
        # Simulación de una tarea que lleva tiempo
        time.sleep(5)
        st.write("¡Contenido actualizado!")

# Agregar contenido fuera del espacio reservado
st.write("Este contenido está fuera del espacio reservado.")


# Función para cargar datos 
@st.cache_data
def load_data():
    file_path = "P07_v07_atribMOVPREFAE_etiq.csv"
    df = pd.read_csv(file_path)
    df["time"]=df.index*7
    column_to_move = 'time'
    columns = [column_to_move] + [col for col in df.columns if col != column_to_move]

    df = df[columns]
    return df

# Cargar datos
data = load_data()

# Mostrar el DataFrame opcionalmente
if st.checkbox("Mostrar Dataset Completo"):
    st.subheader("Vista previa del Dataset")
    st.dataframe(data)

# Selección de variables para graficar
st.sidebar.header("Configuración de Gráficas")
variables = ["Presn", "VelPr", "Des_z", "AcePr"]
column = st.sidebar.selectbox("Selecciona variables para analizar:", variables)


# Configuración del gráfico dinámico
placeholder = st.empty()  # Espacio dinámico para el gráfico

with placeholder.container():
    st.subheader(f"Gráfica de '{column}' vs Tiempo")
    fig, ax = plt.subplots(figsize=(12, 6))
    data.plot(x="time", y=column, ax=ax, color="skyblue", legend=False)
    ax.xaxis.set_minor_locator(MultipleLocator(250))
    ax.set_title(f"Evolución de {column} en el tiempo", fontsize=16)
    ax.set_xlabel("Tiempo", fontsize=12)
    ax.set_ylabel(column, fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.7)
    st.pyplot(fig)
    


