import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
import glob                     # Used for reading files in folder
import os.path                  # Used to save CSV to directory in application
from Scripts.Scripts import scr_calculate_heart_rate_zone, scr_delete_file_popup
from Scripts.Cells import *     # Gather all cell scripts
import os


#region Page Titles

# Display title 
st.header("Load Data", divider=True)

# Display sidebar title
st.sidebar.markdown("Load Data")

# Page Configuration
st.set_page_config(layout="wide")

#endregion Page Titles


#region File System

#region File Upload

# Keep elements wrapped in container
with st.container():

    with st.expander("File System", expanded=True):
        # File upload
        loaded_file = st.file_uploader("Pick a file for upload:", type = "csv")

        if(loaded_file is not None):
            # Read the contents of file loaded
            loaded_file_contents = pd.read_csv(loaded_file)

            # Allow taking uploaded file and sending it to Trial_Data folder
            if st.button("Upload to App", type = "secondary"):
                loaded_file_contents.to_csv(os.path.join("Trial_Data", loaded_file.name))
#endregion File Upload

#region File Selection

        # Create option array
        uploaded_options = ["Select Option"]

        # Find all files located in listed folder and add to array
        for file in glob.glob("Trial_Data/*"):
            uploaded_options.append(file)
            
        # Allow selecting uploaded file for actions
        file_chosen = st.selectbox("Select an uploaded file to view:", options = uploaded_options)

        # Variable to hold contents of file uploaded for actions
        if "file_contents" not in st.session_state:
            st.session_state.file_contents = None

        # If file is selected, allow for action to take place
        if(file_chosen is not "Select Option"):
            # Declares selected file
            selected_file = file_chosen
            # Holds name of file chosen
            file_name = os.path.basename(file_chosen)

            # TODO: Unclear code, requires commenting for further explanation
            df = pd.read_csv(str(file_chosen))
            @st.cache_data
            def convert_for_download(df):
                return df.to_csv().encode("utf-8")
            data = convert_for_download(df)


            # Keeps buttons rendered together in container
            with st.container(horizontal = True, wrap = False):

                # Button allowing for data to be viewed
                if st.button(label="View Data") and selected_file is not None:
                    st.session_state.file_contents = pd.read_csv(selected_file)

                file_contents = st.session_state.file_contents

                # Download file to local drive
                st.download_button(label = "Download File", data = data,file_name=file_name)

                if st.button("Delete File"):
                    #popup for confirming deletion
                    scr_delete_file_popup('Trial_Data',file_name)


#endregion File Selection

#endregion File System


#region Data Visualizer

# Check for valid file contents
if(file_contents is not None):
    options = st.multiselect("What data do you need",["Heart", "Speed", "Acceleration", "Odometry"],default=["Speed", "Acceleration", "Odometry"],)
    # Create columns for data cells
    # Cells listed in columns are in order of rows
    col1, col2, col3 = st.columns(spec=3, width="stretch")

    #region Column 1
    with col1:
        if "Speed" in options:
            cell_speed(file_contents)
        else:
            st.empty()

        if "Heart" in options:
            cell_heart_rate(file_contents)
        else:
            st.empty()

    #endregion Column 1

    #region Column 2
    with col2:
        if "Acceleration" in options:
            cell_acceleration(file_contents)
        else:
            st.empty()

    #endregion Column 2

    #region Column 3
    with col3:
        if "Odometry" in options:
            cell_odometry(file_contents)
        else:
            st.empty()
        

    #endregion Column 3

#endregion Data Visualizer
