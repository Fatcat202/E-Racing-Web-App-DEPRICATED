import streamlit as st           #pip install streamlit
import pandas as pd              #Streamlit dependency
import numpy as np               #Streamlit dependency


#Main file used to control web app



#region Navigation

# TODO: Implement use of navigation buttons to jump to graphs listed


# Addition of E-Racing Logo
st.logo(
    image = "Images/e_racing_logo.PNG",
    size = "large"
)

# Pages
page_welcome = st.Page("Pages/Welcome.py", title = "Welcome", default = True)
page_live_data = st.Page("Pages/Live_Data.py", title = "Live Data")
page_load_data = st.Page("Pages/Load_Data.py", title = "Load Data")
page_driver_dash = st.Page("Pages/Driver_Dash.py", title = "Driver Dash")

# Create navigation list
nav = st.navigation([page_welcome, page_live_data, page_load_data, page_driver_dash])

#Run Navigation object
nav.run()

#endregion Navigation





