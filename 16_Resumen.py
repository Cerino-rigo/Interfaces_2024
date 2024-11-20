import streamlit as st
from datetime import datetime
import time as tm
#Expander in sidebar
st.sidebar.subheader('Expander')
with st.sidebar.expander('Time'):
    time = datetime.now().strftime("%H:%M:%S")
    st.write(f'**{time}**')

#Columns in sidebar
st.sidebar.subheader('Columns')
col1, col2 = st.sidebar.columns(2)
with col1:
    option_1 = st.selectbox('Please select option 1',['A','B'] )
with col2:
    option_2 = st.radio('Please select option 2',['A','B'], index=0)


#Container in sidebar
container = st.sidebar.container()
container.subheader('Container')
option_3 = container.slider('Please select option 3')
st.sidebar.warning('Elements outside of container will be displayed externally')
container.info(f'**Option 3:** {option_3}')

# Crear un espacio reservado con st.empty()
placeholder = st.empty()
#Expander in main body
st.subheader('Expander')
with placeholder.expander('Time'):
    time = datetime.now().strftime("%H:%M:%S")
    st.write(f'**{time}**')

    

#Columns in main body
st.subheader('Columns')
col1, col2 = st.columns(2)
with col1:
    option_4 = st.selectbox('Please select option 4',['A','B'])
with col2:
    option_5 = st.radio('Please select option 5',['A','B'])

#Container in main body
container = st.container()
container.subheader('Container')
option_6 = container.slider('Please select option 6')
st.warning('Elements outside of container will be displayed externally')
container.info(f'**Option 6:** {option_6}')


with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        tm.sleep(1)
    st.write("✔️ 1 minute over!")
