import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
import glob                     # Used for reading files in folder
from Scripts import scr_line_chart, scr_calculate_heart_rate_zone

#Page used to display data from a previous trial

#region Page Titles

# Display title 
st.header("Load Data", divider=True)

# Display sidebar title
st.sidebar.markdown("Load Data")

#endregion Page Titles





#Region Data Loading


# File upload
loaded_file = st.file_uploader("Pick a file for upload:", type = "csv")

if(loaded_file is not None):
    # Read the contents of file loaded
    loaded_file_contents = pd.read_csv(loaded_file)

#endregion Data Loading

#region Download

# Create option array
download_file_options = []

# Find all files located in listed folder and add to array
for file in glob.glob("Trial_Data/*"):
    download_file_options.append(file)
    
# Allow selecting file for download
selected_file = st.multiselect("Select a file to download:", options = download_file_options, max_selections=1, select_all = False)
# If file is selected, allow for downloading file to local system
if(len(selected_file) is not 0):
    st.download_button(label = "Download File", data = selected_file[0])

#endregion Download

    

#region Variables




#endregion Variables


#endregion Variables


#region Data Visualizer

if(loaded_file is not None):

    #region Heart Rate

    # Set to true for testing
    with st.expander("Heart Rate Data"):
        # Check if necessary data types exist
        if(not "Heart Rate" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Heart Rate Data Not Found")
        else:

            # Creating Heart Rate chart
            HR_chart = scr_line_chart(loaded_file, "Time", "Heart Rate")


    #endregion Heart Rate

    #region Suspension

    with st.expander("Suspension Data"):

        #Left Front Suspension
        if(not "LF Suspension" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: LF Suspension Data Not Found")
    # else:
            #TODO: implement left front data graph

        #Right Front Suspension
        if(not "RF Suspension" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: RF Suspension Data Not Found")
    # else:
            #TODO: implement right front data graph

        #Left Rear Suspension
        if(not "LR Suspension" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: LR Suspension Data Not Found")
    # else:
            #TODO: implement left rear data graph

        #Right Rear Suspension
        if(not "RR Suspension" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: RR Suspension Data Not Found")
    # else:
            #TODO: implement right rear data graph

    #endregion Suspension
            
    #region Motor

    with st.expander("Motor Data"):
        if(not "RPM" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Motor Data Not Found")
    #   else:
            #TODO: implement motor data graphs

    #endregion Motor

    #region HV Battery

    with st.expander("HV Battery Data"):
        if(not "HV Charge" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: HV Battery Data Not Found")
    #   else:
            #TODO: implement HV battery data graphs

    #endregion HV Battery

    #region LV Battery

    with st.expander("LV Battery Data"):
        if(not "LV Charge" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: LV Battery Data Not Found")
    #   else:
            #TODO: implement LV battery data graphs

    #endregion LV Battery

    #region Aero Data

    with st.expander("Aero Data"):
        if(not "Aero" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Aero Data Not Found")
    #  else:
            #TODO: implement Aero data graphs

    #endregion Aero Data

    #region Speed

    # Gathered from CAN
    with st.expander("Speed Data"):
        if(not "Speed" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Speed Data Not Found")
    #   else:
            #TODO: implement Speed data graphs

    #endregion Speed

    #region Attitude

    # Gathered from CAN
    with st.expander("Attitude Data"):
        if(not "Attitude" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Attitude Data Not Found")
    #   else:
            #TODO: implement Attitude data graphs

    #endregion Attitude

    #region Odometer

    # Gathered from CAN
    with st.expander("Odometer Data"):
        if(not "Odometer" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Odometer Data Not Found")
        #else:
            #TODO: implement Odometer data graphs

    #endregion Odometer

    #region Acceleration

    # Gathered from CAN
    with st.expander("Acceleration Data"):
        if(not "Acceleration" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Acceleration Data Not Found")
    #   else:
        #TODO: implement Acceleration data graphs (mohammed-done)

    #endregion Acceleration

    #region Angular Data

    # Gathered from CAN
    with st.expander("Angular Data"):
        if(not "Angular" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Angular Data Not Found")
    # else:
        #TODO: implement Angular data graphs

    #endregion Angular Data

    #region Vibration Data

    with st.expander("Vibration Data"):
        if(not "Vibration" in loaded_file_contents or not "Time" in loaded_file_contents):
            st.error("Error: Vibration Data Not Found")
    # else:
        #TODO: implement Vibration data graphs

    #endregion Vibration Data

    #endregion Data Visualizer


