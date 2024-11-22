import streamlit as st  

# Inject custom CSS to set the width of the sidebar and style the content  
st.markdown(  
    """  
    <style>  
        section[data-testid="stSidebar"] {  
            width:230px !important; /* Set the width to your desired value */  
        }  

        /* Custom styles for sidebar */  
        .sidebar-header {  
            font-size: 24px;  
            font-weight: bold;  
            color: #4CAF50; /* Green color */  
        }  

        .sidebar-text {  
            font-size: 16px;  
            color: #333; /* Darker text */  
        }  

        /* Custom styles for main content */  
        .main-header {  
            font-size: 28px;  
            font-weight: bold;  
            color: #FF5722; /* Orange color */  
        }  

        .main-text {  
            font-size: 18px;  
            line-height: 1.5; /* Increase line spacing */  
            color: #444; /* Slightly lighter text */  
        }  
    </style>  
    """,  
    unsafe_allow_html=True,  
)  

# Example sidebar content  
st.sidebar.markdown('<p class="sidebar-header">This is the sidebar</p>', unsafe_allow_html=True)  
st.sidebar.markdown('<p class="sidebar-text">This is some text inside the sidebar</p>', unsafe_allow_html=True)  

# Example main content  
st.markdown('<p class="main-header">This is the Main Content Area</p>', unsafe_allow_html=True)  
st.markdown('<p class="main-text">This is some text in the main content area. You can style it however you like!</p>', unsafe_allow_html=True)