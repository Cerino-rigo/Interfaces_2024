import os
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import streamlit as st


# Función para cargar y procesar datos
@st.cache_data
def load_and_process_data(filepath):
    data = pd.read_csv(filepath)
    #data["Distancia"] = data.apply(lambda row: distance(row["Des_x"], row["Des_y"], row["Des_z"]), axis=1)
    return data

# Función para calcular la distancia
@st.cache_data
def distance(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

# Función para calcular distancias máximas de las sesiones
def calcular_distancias_maximas(sessions):
    return pd.DataFrame(
        [session["Distancia"].sum() for session in sessions],
        columns=["DistMax"],
        index=[f"session{i + 1}" for i in range(len(sessions))]
    )

# Función para graficar variables vs tiempo en subgráficas
def graficar_variables_vs_tiempo(sessions, selected_columns):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
    axs = axs.flatten()

    for i, (session_name, session_data) in enumerate(sessions.items()):
        if i >= 4:  # Limitar a 4 sesiones
            break
        for col in selected_columns:
            session_data.plot(x="time", y=col, ax=axs[i], label=f"{col} - {session_name}")
        axs[i].set_title(f"Sesión: {session_name}", fontsize=14)
        axs[i].set_xlabel("Tiempo", fontsize=12)
        axs[i].set_ylabel("Valor", fontsize=12)
        axs[i].grid(True, linestyle="--", alpha=0.7)
        axs[i].legend()

    plt.tight_layout()
    return fig

# Configuración del directorio de datos
data_dir = "C:/Users/cerin/Tec Semestre agosto/Analítica de datos II/DatosTec/Datos_procesados"

# Configuración de la página
st.set_page_config(page_title="Dashboard de Pacientes", layout="wide")

# CSS para asegurar alturas consistentes de los encabezados
st.markdown("""
    <style>
        .stHeading {
            
            text-align: center;
           
        }
        h1 {  
            height: 100px; /* Altura fija para los encabezados */
           
            font-size: 2.5em; /* Size of the main title */  
            color: #4CAF50; /* Green color for main title */  
            margin-bottom: 50px; /* Margin below the title */  
        }  

        h2 {  
            height: 60px; /* Altura fija para los encabezados */
            font-size: 1.5em; /* Size of secondary headers */  
            color: #FF5722; /* Orange color for secondary headers */  
            margin-bottom: 30px; /* Margin below the title */  
          
        } 
    </style>
""", unsafe_allow_html=True)

#st.title("Dashboard Interactivo de Pacientes")
st.markdown('<h1 class="stHeading">Dashboard Interactivo de Pacientes</h1>', unsafe_allow_html=True)

# Función para seleccionar archivo de datos
def select_data_files(data_dir):
    patients = ["P07", "P08", "P11"]
    selected_patient = st.sidebar.selectbox("Selecciona un paciente:", patients)

    if selected_patient:
        sessions_dir = os.path.join(data_dir, selected_patient)
        sessions = sorted([folder for folder in os.listdir(sessions_dir) if os.path.isdir(os.path.join(sessions_dir, folder))])
        selected_sessions = st.sidebar.multiselect("Selecciona sesiones:", sessions, default=sessions[:1])

        ventaneo_options = ["03", "05", "07", "09", "11"]
        selected_ventaneo = st.sidebar.selectbox("Selecciona un ventaneo:", ventaneo_options)

        session_files = {}
        for session in selected_sessions:
            session_path = os.path.join(sessions_dir, session)
            for file in os.listdir(session_path):
                if f"v{selected_ventaneo}" in file and file.endswith(".csv"):
                    session_files[session] = os.path.join(session_path, file)
                    break

        return session_files
    return {}

selected_files = select_data_files(data_dir)

if selected_files:
    # Cargar los datos seleccionados
    sessions_data = {name: load_and_process_data(path) for name, path in selected_files.items()}

    # Variables seleccionadas por el usuario
    available_columns = list(sessions_data[list(sessions_data.keys())[0]].columns[1:])
    selected_columns = st.sidebar.multiselect(
        "Selecciona las columnas para analizar:",
        options=available_columns,
        default=available_columns[:2]
    )

    # Distribución en columnas
    col1, col2 = st.columns(2)

    # Columna 1: Gráficas de variables vs tiempo
    with col1:
        #st.header("Variables vs Tiempo")
        st.markdown('<h2 class="stHeading">Variables vs Tiempo</h2>', unsafe_allow_html=True)
        if selected_columns:
            fig_variables = graficar_variables_vs_tiempo(sessions_data, selected_columns)
            st.pyplot(fig_variables)
        else:
            st.warning("Selecciona al menos una columna para analizar.")

    # Columna 2: Distancias máximas
    with col2:
        #st.header("Distancias Máximas por Sesión")
        st.markdown('<h2 class="stHeading">Distancias Máximas por Sesión</h2>', unsafe_allow_html=True)
        dists_max = calcular_distancias_maximas(list(sessions_data.values()))

        fig_dists, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(dists_max.index, dists_max["DistMax"], color=plt.get_cmap("Set1").colors[:len(dists_max)])
        ax.set_title("Distancias Máximas", fontsize=16)
        ax.set_xlabel("Sesión", fontsize=12)
        ax.set_ylabel("Distancia Máxima", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.7)

        for bar in bars:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{bar.get_height():.1f}",
                ha="center", va="bottom"
            )

        st.pyplot(fig_dists)
else:
    st.warning("Selecciona un paciente, sesión y ventaneo válidos para continuar.")
