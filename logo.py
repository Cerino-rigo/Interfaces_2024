import streamlit as st  



col1, col2 = st.columns([0.95, 0.05])
with col1:
    st.subheader("Aplicación principal")
with col2: 
    st.image(
        image="Logo_del_ITESM.svg.png", width=45,       
    )

# Título y descripción  
st.title("Mi Aplicación")  
st.subheader("Esta es una aplicación de ejemplo con un logo personalizado.") 


st.image(
        image="Logo_del_ITESM.svg.png"
)