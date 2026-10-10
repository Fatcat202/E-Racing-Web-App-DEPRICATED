import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #pip install csv
import time                     #pip install time
import pathlib as pl            # pip install pathlib
from Scripts import scr_calculate_heart_rate_zone
#from streamlit_autorefresh import st_autorefresh # pip install streamlit_autorefresh


#Page used to display live data


#Region Data Loading

# TODO Load data from network

# Holds file loaded
data_file = None



#endregion Data Loading


#region Variables

# Declares if a live connection to data is established, default false
live_connection = False



#endregion Variables


#region Page Titles

# Display title
st.header("Live Data", divider=True)
# Display sidebar title
st.sidebar.markdown("Live Data")


# Widget showing if connection to live data is active
csv_file_content = pd.read_csv("Trial_Data/canmod_gps_data.csv")
with st.sidebar:
    if csv_file_content is not None:
        st.success("Live")
    elif csv_file_content is None:
        st.error("No Data Stream")
    else:
        st.error("No Data Stream")

#endregion Page Titles


#region Data Visualizer

# Check if a live connection is made
if(live_connection == True):

    # Read the contents of file loaded
    data_file_contents = pd.read_csv(data_file) 

    #region Heart Rate

    # Set to true for testing
    with st.expander("Heart Rate Data"):
        # Check if necessary data types exist
        if(not "Heart Rate" in data_file_contents or not "Time" in data_file_contents):
            st.error("Error: Heart Rate Data Not Found")
        else:

            # Most recently read heart rate data
            active_heart_rate = data_file_contents["Heart Rate"].iloc[-1]

            # Creating Heart Rate chart
            HR_chart = st.line_chart(data=data_file_contents, x="Time", y="Heart Rate")

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


    #endregion Heart Rate


#endregion Data Visualizer

# region CAN sensors
#placeholder4 = st.empty()
#placeholder3 = st.empty()
#placeholder2 = st.empty()
#placeholder1 = st.empty()
#active_Speed_rate = csv_file_content["AccelerationX"]#.iloc[-1]
#active_DistanceTotal_rate = csv_file_content["AngularRateX"]#.iloc[-1]
#active_AngularRateX_rate = csv_file_content["t"]#.iloc[-1]
#active_AccelerationX_rate = csv_file_content["message_name"]#.iloc[-1]
#st.write(active_Speed_rate)

#Important_messages = {
 #   "Speed": ("Speed"),
  #  "IMU": ("AccelerationX", "AngularRateX"),
   # "Odo": ("DistanceTotal")
#}

#st_autorefresh(interval=1000, key="Acceleration_refresh")
#placeholder4.metric(
#"🏎 Acceleration",
#f"{active_AccelerationX_rate:.1f}"
#)

#st_autorefresh(interval=1000, key="AngularVelocity_refresh")
#placeholder3.metric(
#"🏎 Angular Velocity",
#f"{active_AngularRateX_rate:.1f}"
#)

#st_autorefresh(interval=1000, key="Distance_refresh")
#placeholder2.metric(
#"🏎 Distance Travelled",
#f"{active_DistanceTotal_rate:.1f}"
#)

#time.sleep(1)

#st_autorefresh(interval=1000, key="Speed_refresh")
#placeholder1.metric(
#"🏎 Current Speed",
#f"{active_Speed_rate:.1f}"
#)

#time.sleep(1)

# endregion CAN sensors


