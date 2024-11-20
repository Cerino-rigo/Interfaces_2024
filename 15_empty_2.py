import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuración de página
st.set_page_config(page_title="Análisis de Variables vs Tiempo", page_icon="⏱️")
st.title("Comparación de Variables vs Tiempo")

# Función para cargar datos
@st.cache_data
def load_data():
    file_path = "P07_v07_atribMOVPREFAE_etiq.csv"
    df = pd.read_csv(file_path)
    df["time"] = df.index * 7
    column_to_move = "time"
    columns = [column_to_move] + [col for col in df.columns if col != column_to_move]
    return df[columns]

# Cargar datos
data = load_data()

# Mostrar el DataFrame opcionalmente
if st.checkbox("Mostrar Dataset Completo"):
    st.subheader("Vista previa del Dataset")
    st.dataframe(data)

# Multiselección de columnas para graficar
st.sidebar.header("Configuración de la Visualización")
selected_columns = st.sidebar.multiselect(
    "Selecciona las columnas para analizar:",
    options=data.columns[1:],  # Excluir "time"
    default=[data.columns[1]]  # Primera columna seleccionada por defecto
)

# Obtener todas las paletas de colores disponibles en Matplotlib
available_palettes = plt.colormaps()

# Selección de paletas de colores (multiselección)
color_palette = st.sidebar.selectbox(
    "Selecciona las paletas de colores:",
    options=available_palettes,
    
)

# Mostrar estadísticas descriptivas
if selected_columns:
    st.subheader("Análisis Estadístico")
    stats = data[selected_columns].describe().T
    st.table(stats)

# Configuración del gráfico dinámico
placeholder = st.empty()  # Espacio dinámico para el gráfico

if selected_columns:
    with placeholder.container():
        st.subheader(f"Gráfica de {', '.join(selected_columns)} vs Tiempo")
        fig, ax = plt.subplots(figsize=(12, 6))

        # Crear un colormap basado en la paleta seleccionada
        cmap = plt.get_cmap(color_palette)
        colors = cmap(np.linspace(0, 1, len(selected_columns)))

        # Graficar cada columna seleccionada
        for col, color in zip(selected_columns, colors):
            data.plot(x="time", y=col, ax=ax, color=color, legend=True, label=col)

        ax.set_title(f"Evolución de {', '.join(selected_columns)} en el tiempo", fontsize=16)
        ax.set_xlabel("Tiempo", fontsize=12)
        ax.set_ylabel("Valor", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.7)
        st.pyplot(fig)
else:
    st.warning("Por favor, selecciona al menos una columna para analizar.")
