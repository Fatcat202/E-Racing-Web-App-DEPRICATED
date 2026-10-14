import streamlit as st          # pip install streamlit
import pandas as pd             # streamlit dependency
from Scripts.Scripts import scr_calculate_heart_rate_zone


#region Heart Rate
def cell_heart_rate(file_contents, x_axis, live_connection=False):
    # Pass through file contents, normally selected_file_contents

    with st.container(border=True):

        st.header("Heart Rate Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "Heart Rate" in file_contents or not "Time" in file_contents):
            st.error("Error: Heart Rate Data Not Found")
        else:
            # Creating Heart Rate chart
            if x_axis == "time":
                HR_chart = st.line_chart(data=file_contents, x="Time", y="Heart Rate" , x_label="Time (S)")
            elif x_axis == "distance":
                HR_chart = st.line_chart(data=file_contents, x="Distance", y="Heart Rate" , x_label="Distance (m)")

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
        if(not "Distance" in file_contents or not "time" in file_contents):
            st.error("Error: Odometry Data Not Found")
        else:
            # Creating odometry chart
            odometry_chart = st.line_chart(data=file_contents, x="time", y="Distance", x_label="Time (s)")
#endregion Odometry Data

#region Acceleration Data
def cell_acceleration(file_contents, x_axis):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Acceleration Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "Acceleration" in file_contents or not "time" in file_contents):
            st.error("Error: Acceleration Data Not Found")
        else:
            # Creating acceleration chart
            if x_axis == "time":
                accel_chart = st.line_chart(data=file_contents, x="time", y="Acceleration", x_label="Time (s)")
            elif x_axis == "distance":
                accel_chart = st.line_chart(data=file_contents, x="Distance", y="Acceleration", x_label="Distance (m)")
#endregion Acceleration Data

#region Speed Data
def cell_speed(file_contents, x_axis):
    with st.container(border=True):
        st.header("Speed Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "Speed" in file_contents or not "time" in file_contents):
            st.error("Error: Speed Data Not Found")
        else:
            # Creating Speed chart
            if x_axis == "time":
                accel_chart = st.line_chart(data=file_contents, x="time", y="Speed", x_label="Time (s)")
            elif x_axis == "distance":
                accel_chart = st.line_chart(data=file_contents, x="Distance", y="Speed", x_label="Distance (m)")
#endregion Speed Data

#region Attitude Data
def cell_attitude(file_contents):
    with st.container(border=True):
        st.header("Attitude Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "Heading" in file_contents or not "time" in file_contents or not "Pitch" in file_contents or not "Roll" in file_contents):
            st.error("Error: Speed Data Not Found")
        else:
            # Creating speed chart
            speed_graph = st.line_chart(data=file_contents, x="time", y=["Heading","Pitch","Roll"], x_label="Time (s)", y_label="Attitude")
#endregion Speed Data