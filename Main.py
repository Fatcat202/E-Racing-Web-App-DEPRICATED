import streamlit as st           #pip install streamlit
import pandas as pd              #Streamlit dependency
import numpy as np               #Streamlit dependency


#Main file used to control web app



#region Navigation

# TODO: Implement use of navigation buttons to jump to graphs listed


# Addition of E-Racing Logo
st.logo(
    image = "Images/e_racing_logo.png",
    size = "large"
)

# Pages
page_welcome = st.Page("pages/Welcome.py", title = "Welcome", default = True, icon="📍")
page_live_data = st.Page("pages/Live_Data.py", title = "Live Data", icon="📍")
page_load_data = st.Page("pages/Load_Data.py", title = "Load Data", icon="📂")
page_driver_dash = st.Page("pages/Driver_Dash.py", title = "Driver Dash", icon="🏎")

# Create navigation list
nav = st.navigation([page_welcome, page_live_data, page_load_data, page_driver_dash])

connection = False
with st.sidebar:
    if connection is False:
        st.success(" Live ")
    else:
        st.error(" No Data Stream")

#Run Navigation object
nav.run()

#endregion Navigation





