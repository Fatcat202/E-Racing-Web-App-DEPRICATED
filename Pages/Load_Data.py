import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
import glob                     # Used for reading files in folder
import os.path                  # Used to save CSV to directory in application
from Scripts import scr_calculate_heart_rate_zone, scr_delete_file_popup
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
        selected_file_contents = None

        # If file is selected, allow for action to take place
        if(file_chosen is not "Select Option"):
            # Declares selected file
            selected_file = file_chosen
            # Holds name of file chosen
            selected_file_name = os.path.basename(file_chosen)

            # TODO: Unclear code, requires commenting for further explanation
            df = pd.read_csv(str(file_chosen))
            @st.cache_data
            def convert_for_download(df):
                return df.to_csv().encode("utf-8")
            data = convert_for_download(df)


            # Keeps buttons rendered together in container
            with st.container(horizontal = True, wrap = False):

                # Button allowing for data to be viewed
                if st.button(label = "View Data") and selected_file is not None:
                    selected_file_contents = pd.read_csv(selected_file)

                # Download file to local drive
                st.download_button(label = "Download File", data = data,file_name=selected_file_name)

                if st.button("Delete File"):
                    #popup for confirming deletion
                    scr_delete_file_popup('Trial_Data',selected_file_name)


#endregion File Selection

#endregion File System


#region Data Visualizer

if(selected_file_contents is not None):

    #region Heart Rate

    # Set to true for testing
    with st.expander("Heart Rate Data"):
        # Check if necessary data types exist
        if(not "Heart Rate" in selected_file_contents or not "Time" in selected_file_contents):
            st.error("Error: Heart Rate Data Not Found")
        else:

            # Creating Heart Rate chart
            HR_chart = st.line_chart(data=selected_file_contents, x="Time", y="Heart Rate")


    #endregion Heart Rate

    with st.expander("Speed data"):
        # Check if necessary data types exist
        if(not "Speed" in selected_file_contents or not "t" in selected_file_contents):
            st.error("Error: Speed Data Not Found")
        else:

            # Creating Speed chart
            Speed = st.line_chart(data=selected_file_contents, x="time", y="Speed")

    with st.expander("Odometry Data"):
        # Check if necessary data types exist
        if(not "Distance" in selected_file_contents or not "time" in selected_file_contents):
            st.error("Error: Odometry Data Not Found")
        else:

            # Creating Heart Rate chart
            Speed = st.line_chart(data=selected_file_contents, x="time", y="Distance")

    with st.expander("Acceleration Data"):
        # Check if necessary data types exist
        if(not "Acceleration" in selected_file_contents or not "time" in selected_file_contents):
            st.error("Error: Acceleration Data Not Found")
        else:

            # Creating Heart Rate chart
            Speed = st.line_chart(data=selected_file_contents, x="time", y="Acceleration")

    #endregion Data Visualizer
