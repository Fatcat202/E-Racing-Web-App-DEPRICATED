import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
import glob                     # Used for reading files in folder
import os.path                  # Used to save CSV to directory in application
from Scripts import scr_calculate_heart_rate_zone


#Page used to display data from a previous trial

#region Page Titles

# Display title 
st.header("Load Data", divider=True)

# Display sidebar title
st.sidebar.markdown("Load Data")

#endregion Page Titles





#Region File Upload

# Keep elements wrapped in container
with st.container():
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
    selected_file_name = str(file_chosen)

    # Keeps buttons rendered together in container
    with st.container(horizontal = True, wrap = False):
        # Download file to local drive
        st.download_button(label = "Download File", data = selected_file[0])

        # Button allowing for data to be viewed
        if st.button(label = "View Data") and selected_file is not None:
            selected_file_contents = pd.read_csv(selected_file)
        

#endregion File Selection


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

    

    #endregion Data Visualizer


