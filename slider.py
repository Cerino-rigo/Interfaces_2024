import streamlit as st  
import numpy as np  
import plotly.express as px  
import pandas as pd  

 
def generate_plot(i):  
    
    x = np.linspace(0, 10, 100)  # 100 puntos de 0 a 10  
    y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)  # Seno con ruido  

    
    df = pd.DataFrame({'x': x, 'y': y})  

    # Crear la gráfica  
    fig = px.line(df, x='x', y='y', title=f'Gráfica {i}', labels={'x': 'Eje X', 'y': 'Eje Y'})  
    
    return fig  

# Definir opciones y rangos para el slider  
opciones = [1, 6, 11]  
min_value = min(opciones)  
max_value = max(opciones)  

# Slider con rango de valores  
valores = st.slider("Selecciona un rango de gráficas a desplegar", min_value=1, max_value=12, value=(1, 6), step=6)  
st.write(f"min: {valores[0]}, max: {valores[1]}")
# Ajustar el límite inferior dependiendo del límite superior  
if valores[0]  == 1 and valores[1] >= 12:  
    limites = (1, 6)  
elif valores[0]  == 6 and valores[1] >= 12 :  
    limites = (6, 12)  
else:   
    limites = valores  

st.write("Valores de gráficas seleccionadas:", limites)  

# Validar que se muestren las gráficas según los límites ajustados  
for i in range(limites[0], limites[1]+1):  
    st.plotly_chart(generate_plot(i))