import streamlit as st
import pandas as pd
import numpy as np

 
if 'counter' not in st.session_state:  
    st.session_state.counter = 0  

if st.button('Run'):  
    st.session_state.counter += 1  

st.write(f'Counter: {st.session_state.counter}') 

# Funciones de análisis para cada tienda
def sesion_1(paciente):
    st.write("Análisis para la sesión 1")
    st.write(paciente.head())

def sesion_2(paciente):
    st.write("Análisis para la sesión 2")
    st.write(paciente.head())

def sesion_3(paciente):
    st.write("Análisis para la sesión 3")
    st.write(paciente.head())

# Sidebar
st.sidebar.title("Configuración")

paciente_seleccionado = st.sidebar.radio(":hospital: Seleccionar paciente", ["Paciente 7", "Paciente 8", "Paciente 11"])

tipo_grafico = st.sidebar.selectbox(":bar_chart: Seleccionar Tipo de Gráfico", ["Gráfico de Barras", "Gráfico de Líneas", "Scatter Plot"])

# Datos de ejemplo
data = {
    'Paciente 7': np.random.randint(1, 100, 100),
    'Paciente 8': np.random.randint(1, 100, 100),
    'Paciente 11': np.random.randint(1, 100, 100)
}
df = pd.DataFrame(data)

if 'button' not in st.session_state:
        st.session_state.button = False

def click_button():
        st.session_state.button = not st.session_state.button

# Botones en la parte superior
col1, col2, col3 = st.columns(3)
if col1.button(":spiral_calendar_pad: **Sesión 1**", help="Haz clic para ver análisis de la sesión 1", use_container_width=True):
    sesion_1(df["Paciente 7"])

if col2.button(":spiral_note_pad: $\t Sesión 2$", help="Haz clic para ver análisis de la sesión 2", use_container_width=True):
    sesion_2(df["Paciente 8"])


if col3.button(":hospital: Sesión 3", help="Haz clic para ver análisis de la sesión 3", use_container_width=True, on_click=click_button):
    if st.session_state.button:
        sesion_3(df["Paciente 11"])

    
# Línea divisoria visual
st.markdown('---')
st.markdown('<hr style="border: 2px solid #CB1A2D; background-color: #3498db; height: 5px;">', unsafe_allow_html=True)
    

# Agregar gráfico según la selección
if tipo_grafico == "Gráfico de Barras":
    st.bar_chart(df[paciente_seleccionado])
elif tipo_grafico == "Gráfico de Líneas":
    st.line_chart(df[paciente_seleccionado])
elif tipo_grafico == "Scatter Plot":
    st.scatter_chart(df[paciente_seleccionado])
