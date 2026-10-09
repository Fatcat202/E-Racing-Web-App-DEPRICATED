import streamlit as st          # pip install streamlit
import pandas as pd             # streamlit dependency
from Scripts.Scripts import scr_calculate_heart_rate_zone


#region Heart Rate
def cell_heart_rate(file_contents, live_connection=False):
    # Pass through file contents, normally selected_file_contents

    with st.container(border=True):

        st.header("Heart Rate Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "Heart Rate" in file_contents or not "Time" in file_contents):
            st.error("Error: Heart Rate Data Not Found")
        else:
            # Creating Heart Rate chart
            HR_chart = st.line_chart(data=file_contents, x="Time", y="Heart Rate")

            if(live_connection == True):
                # Numerical input for driver age
                driver_age = 0
                driver_age = st.number_input("Enter Driver Age:", min_value = 0, max_value = 99)

                # Most recently read heart rate data
                active_heart_rate = file_contents["Heart Rate"].iloc[-1]

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


#region Odometry Data
def cell_odometry(file_contents):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Odometry Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "DistanceTrip" in file_contents or not "time" in file_contents):
            st.error("Error: Odometry Data Not Found")
        else:

            # Creating Heart Rate chart
            odometry_chart = st.line_chart(data=file_contents, x="time", y="DistanceTrip")
#endregion Odometry Data

#region Acceleration Data
def cell_acceleration(file_contents):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Acceleration Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "AccelerationX" in file_contents or not "time" in file_contents):
            st.error("Error: Acceleration Data Not Found")
        else:

            # Creating Heart Rate chart
            accel_chart = st.line_chart(data=file_contents, x="time", y="AccelerationX")
#endregion Acceleration Data

#region Speed Data
def cell_speed(file_contents):
    with st.container(border=True):
        st.header("Speed Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "Speed" in file_contents or not "time" in file_contents):
            st.error("Error: Speed Data Not Found")
        else:

            # Creating Speed chart
            Speed = st.line_chart(data=file_contents, x="time", y="Speed")
#endregion Speed Data