import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
from Scripts import scr_line_chart, scr_calculate_heart_rate_zone
import time

#Page used to display live data


#Region Data Loading

# Hard coded placeholder data
testing_file = "Trial_Data/data.csv"
# TODO Load data from network

# Holds file loaded
data_file = testing_file

# Read the contents of file loaded
data_file_contents = pd.read_csv(data_file)




#endregion Data Loading


#region Variables

# Declares if a live connection to data is established, default false
live_connection = False

# Most recently read heart rate data
active_heart_rate = data_file_contents["Heart Rate"].iloc[-1]



#endregion Variables


#region Page Titles

# Display title
st.header("Live Data", divider=True)
# Display sidebar title
st.sidebar.markdown("Live Data")


# Widget showing if connection to live data is active
with st.sidebar:
    if live_connection is True:
        st.success("Live")
    else:
        st.error("No Data Stream")

#endregion Page Titles


#region Data Visualizer

#region Heart Rate

# Set to true for testing
with st.expander("Heart Rate Data"):
    # Check if necessary data types exist
    if(not "Heart Rate" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Heart Rate Data Not Found")
    else:

        # Creating Heart Rate chart
        HR_chart = scr_line_chart(data_file, "Time", "Heart Rate")

        # Numerical input for driver age
        driver_age = 0
        driver_age = st.number_input("Enter Driver Age:", min_value = 0, max_value = 99)

        # Calculate HR data
        percent_HRmax, zone_HR = scr_calculate_heart_rate_zone(active_heart_rate, driver_age)
        # Change from decimal to percent
        percent_HRmax *= 100
        # Modify percent to have a max of 4 digits
        percent_HRmax = f'{percent_HRmax:.4}'

        # Heart rate, Percent, and HR zone display
        col1, col2, col3 = st.columns(3)
        col1.metric(label = "Heart Rate", value = active_heart_rate, border = True)
        col2.metric(label = "HRmax%", value = percent_HRmax, border = True)
        col3.metric(label = "HR Zone", value = zone_HR, border = True)

        #TODO: implement heart rate data graphs

#endregion Heart Rate

#region Suspension

with st.expander("Suspension Data"):

    #Left Front Suspension
    if(not "LF Suspension" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: LF Suspension Data Not Found")
   # else:
        #TODO: implement left front data graph

    #Right Front Suspension
    if(not "RF Suspension" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: RF Suspension Data Not Found")
   # else:
        #TODO: implement right front data graph

    #Left Rear Suspension
    if(not "LR Suspension" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: LR Suspension Data Not Found")
   # else:
        #TODO: implement left rear data graph

    #Right Rear Suspension
    if(not "RR Suspension" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: RR Suspension Data Not Found")
   # else:
        #TODO: implement right rear data graph

#endregion Suspension
         
#region Motor

with st.expander("Motor Data"):
    if(not "RPM" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Motor Data Not Found")
 #   else:
        #TODO: implement motor data graphs

#endregion Motor

#region HV Battery

with st.expander("HV Battery Data"):
    if(not "HV Charge" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: HV Battery Data Not Found")
 #   else:
        #TODO: implement HV battery data graphs

#endregion HV Battery

#region LV Battery

with st.expander("LV Battery Data"):
    if(not "LV Charge" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: LV Battery Data Not Found")
 #   else:
        #TODO: implement LV battery data graphs

#endregion LV Battery

#region Aero Data

with st.expander("Aero Data"):
    if(not "Aero" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Aero Data Not Found")
  #  else:
        #TODO: implement Aero data graphs

#endregion Aero Data

#region Speed

# Gathered from CAN
with st.expander("Speed Data"):
    if(not "Speed" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Speed Data Not Found")
 #   else:
        #TODO: implement Speed data graphs

#endregion Speed

# region laptime

with st.expander("Lap Timing"):
    if "lap_start" not in st.session_state:
        st.session_state.lap_start = time.time() # lap start value is equal to time when it starts 
    current_lap = time.time() - st.session_state.lap_start # calculates current lap time 
    if "best timing" not in st.session_state: 
        st.session_state.best_lap = 151.328 # simulation replace later with current lap time compared to previous laps 
        track_position = 4 # simulath csv data ion we could replace later with csv
        col1, col2, col3 = st.columns(3) # 3 columns for current lap time, best lap time and the difference between them 
        col1.metric(
            label=" Current Lap",
            value=f"{current_lap:.3f}s"
        )# current lap time 
        col2.metric(
            label="Best Lap",
            value=f"{st.session_state.best_lap:.3f}s"
        )# best lap time

        delta = current_lap - st.session_state.best_lap # calculate difference between current recorded lap time and best recorded laptime
        col3.metric(
            label="Delta",
            value=f"{delta:+.3f}s"
        )# display delta
        st.button("Finish Lap") # later will be automated using CANmod.gps

        if current_lap < st.session_state.best_lap: # if the current recorded lap is faster than the best recorded
            st.session_state.best_lap = current_lap # update the best lap record 
            st.session_state.lap_start = time.time() # reset time for a new lap
            st.success("New lap started")
#end region laptime

#region Attitude

# Gathered from CAN
with st.expander("Attitude Data"):
    if(not "Attitude" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Attitude Data Not Found")
 #   else:
        #TODO: implement Attitude data graphs

#endregion Attitude

#region Odometer

# Gathered from CAN
with st.expander("Odometer Data"):
    if(not "Odometer" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Odometer Data Not Found")
    #else:
        #TODO: implement Odometer data graphs

#endregion Odometer

#region Acceleration

# Gathered from CAN
with st.expander("Acceleration Data"):
    if(not "Acceleration" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Acceleration Data Not Found")
 #   else:
    #TODO: implement Acceleration data graphs (mohammed-done)

#endregion Acceleration

#region Angular Data

# Gathered from CAN
with st.expander("Angular Data"):
 if(not "Angular" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Angular Data Not Found")
# else:
    #TODO: implement Angular data graphs

#endregion Angular Data

#region Vibration Data

with st.expander("Vibration Data"):
 if(not "Vibration" in data_file_contents or not "Time" in data_file_contents):
        st.error("Error: Vibration Data Not Found")
# else:
     #TODO: implement Vibration data graphs

#endregion Vibration Data


#endregion Data Visualizer



