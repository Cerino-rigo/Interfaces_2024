import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Función para cargar datos
def load_and_process_data(filepath):
    data = pd.read_csv(filepath)
    return data

# Función para calcular los intervalos de sentimiento
def calculate_intervals(data, sentiment_columns):
    intervals_dict = {col: [] for col in sentiment_columns}
    for col in sentiment_columns:
        start = None
        for j in range(len(data)):
            if data[col].iloc[j] == 1:
                if start is None:
                    start = data['time'].iloc[j]
            else:
                if start is not None:
                    end = data['time'].iloc[j - 1]
                    intervals_dict[col].append((start, end))
                    start = None
        if start is not None:  # Capturar el último intervalo
            intervals_dict[col].append((start, data['time'].iloc[-1]))
    return intervals_dict

# Función para graficar intervalos de sentimiento
def plot_sentiment_intervals(intervals_dict, sentiment_columns, session_title):
    fig, ax = plt.subplots(figsize=(20, 5))
    color_map = plt.get_cmap("Set1").colors  # Colores para cada sentimiento

    for i, col in enumerate(sentiment_columns):
        intervals = intervals_dict[col]
        for (start, end) in intervals:
            ax.hlines(y=i, xmin=start, xmax=end, color=color_map[i], linewidth=6)

    # Etiquetas y formato
    ax.set_yticks(range(len(sentiment_columns)))
    ax.set_yticklabels(sentiment_columns)
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Sentimientos")
    ax.set_title(f"Presencia de sentimientos en intervalos de tiempo - {session_title}")
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return fig

# Estructura interactiva del dashboard
st.title("Dashboard Interactivo de Sentimientos por Paciente y Sesión")

# Directorio de datos procesados
data_dir = "C:/Users/cerin/Tec Semestre agosto/Analítica de datos II/DatosTec/Datos_procesados"


def select_data_file(data_dir):
    """
    Función para seleccionar un archivo de datos basado en la estructura jerárquica de directorios (paciente -> sesión -> archivo de ventaneo).
    
    Args:
        data_dir (str): Ruta al directorio raíz donde se encuentran los datos procesados.

    Returns:
        str: Ruta completa del archivo seleccionado.
        None: Si no se selecciona un archivo.
    """
    # Selección de paciente
    #Devuelve una lista ordenada de los nombres de las carpetas que representan pacientes en data_dir.
    # os.path.join(data_dir, folder) crea la ruta completa hacia cada elemento para verificar si es una carpeta.
    patients = sorted([folder for folder in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, folder))])
    selected_patient = st.sidebar.selectbox("Selecciona un paciente:", patients)

    if selected_patient:
        # Listar sesiones del paciente seleccionado
        sessions_dir = os.path.join(data_dir, selected_patient)
        sessions = sorted([folder for folder in os.listdir(sessions_dir) if os.path.isdir(os.path.join(sessions_dir, folder))])
        selected_session = st.sidebar.selectbox("Selecciona una sesión:", sessions)

        if selected_session:
            # Listar archivos de ventaneo en la sesión seleccionada
            session_path = os.path.join(sessions_dir, selected_session)
            ventaneo_files = sorted([file for file in os.listdir(session_path) if file.endswith(".csv")])
            selected_file = st.sidebar.selectbox("Selecciona un archivo de ventaneo:", ventaneo_files)

            if selected_file:
                # Retornar ruta completa del archivo seleccionado
                return os.path.join(session_path, selected_file)

    return None  # Si no se selecciona un archivo

selected_file_path = select_data_file(data_dir)


data = load_and_process_data(selected_file_path)

            # Columnas de sentimientos
sentiment_columns = ['01_C', '02_A', '03_D', '04_M']
if all(col in data.columns for col in sentiment_columns):
                # Calcular intervalos y graficar
    intervals_dict = calculate_intervals(data, sentiment_columns)
    fig = plot_sentiment_intervals(intervals_dict, sentiment_columns, selected_file_path)
    st.pyplot(fig)
else:
    st.error("Las columnas de sentimientos no están presentes en los datos seleccionados.")
