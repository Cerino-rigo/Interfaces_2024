import streamlit as st  

# Inject custom CSS to set consistent heights and styles for headers  
st.markdown("""  
<style>  
.stHeading {  
   
    text-align: center;  
     
}  

h1 {  
    font-size: 2.5em; /* Size of the main title */  
    color: #4CAF50; /* Green color for main title */  
    margin-bottom: 30px; /* Margin below the title */  
}  

h2 {  
    font-size: 2em; /* Size of secondary headers */  
    color: #FF5722; /* Orange color for secondary headers */  
    margin-bottom: 50px; /* Margin below secondary headers */  
}  

h3 {  
    font-size: 1.5em; /* Size of tertiary headers */  
    color: #2196F3; /* Blue color for tertiary headers */  
    margin-bottom: 10px; /* Margin below tertiary headers */  
}  
</style>  
""", unsafe_allow_html=True)  

# Main Title  
st.markdown('<h1 class="stHeading">Este es el Título Principal</h1>', unsafe_allow_html=True)  

# Subheader Level 1  
st.markdown('<h2 class="stHeading">Este es un Encabezado Secundario</h2>', unsafe_allow_html=True)  

# Subheader Level 2  
st.markdown('<h3 class="stHeading">Este es un Encabezado Terciario</h3>', unsafe_allow_html=True)  

# Add some main content  
st.write("Aquí hay algún contenido relacionado.")