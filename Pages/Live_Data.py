import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
from Scripts.Scripts import scr_calculate_heart_rate_zone
from Scripts.Cells import *


#Page used to display live data

#region Variables

# Declares if a live connection to data is established, default false
live_connection = False

#endregion Variables

#Region Data Loading

# TODO Load data from network/port, setting live_connection to true

# Holds file loaded
data_file = None

# Holds contents of file. Filled in data visualiser
file_contents = None

#endregion Data Loading

#region Page Titles

# Display title
st.header("Live Data", divider=True)
# Display sidebar title
st.sidebar.markdown("Live Data")

# Page Configuration
st.set_page_config(layout="wide")

# Widget showing if connection to live data is active
with st.sidebar:
    if live_connection is True:
        st.success("Live")
    else:
        st.error("No Data Stream")

#endregion Page Titles


#region Data Visualizer

# Check for valid file contents, a live connection made
if(file_contents != None and live_connection == True):

    # Read the contents of file loaded
    file_contents = pd.read_csv(data_file) 

    # Create columns for data cells
    # Cells listed in columns are in order of rows
    col1, col2, col3 = st.columns(spec=3, width="stretch")

    #region Column 1
    with col1:

        cell_speed(file_contents)

        cell_heart_rate(file_contents, live_connection=live_connection)

    #endregion Column 1

    #region Column 2
    with col2:

        cell_acceleration(file_contents)

    #endregion Column 2

    #region Column 3
    with col3:

        cell_odometry(file_contents)

    #endregion Column 3

#endregion Data Visualizer

