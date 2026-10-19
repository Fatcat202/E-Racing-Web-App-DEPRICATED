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
#endregion Attutide Data

#region Motor Data
#region Current A(RMS) Data
def cell_motor_current(file_contents):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Current Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "1. Current A(RMS) (1)" in file_contents or not "1. Velocity RPM (1)" in file_contents):
            st.error("Error: current Data Not Found")
        else:
            # Creating current chart
            current_chart = st.line_chart(data=file_contents, x="1. Current A(RMS) (1)", y="1. Velocity RPM (1)", x_label="Current A(RMS)", y_label="Velocity RPM")
#endregion Current A(RMS) Data

#region Motor Temp
def cell_motor_temp(file_contents):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Motor Temp Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "1. Motor Temperature/Torque Cutback  (0.00390625)" in file_contents or not "Time (s)" in file_contents):
            st.error("Error: motor_temp Data Not Found")
        else:
            # Creating motor_temp chart
            motor_temp_chart = st.line_chart(data=file_contents, x="Time (s)", y="1. Motor Temperature/Torque Cutback  (0.00390625)", y_label="Temperautre")
#endregion Motor Temp


#region Capacitor Voltage
def cell_motor_capacitor_voltage(file_contents):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Capacitor Voltage Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "1. Current A(RMS) (1)" in file_contents or not "1. Capacitor Voltage V (0.0625)" in file_contents):
            st.error("Error: capacitor_voltage Data Not Found")
        else:
            # Creating capacitor_voltage chart
            capacitor_voltage_chart = st.line_chart(data=file_contents, x="1. Current A(RMS) (1)", y="1. Capacitor Voltage V (0.0625)", x_label="Current A(RMS)", y_label="Capacitor Voltage")
#endregion Capacitor Voltage

#region Torque Demand Value
def cell_motor_torque_demand_value(file_contents):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Torque Demand Value Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "1. Torque demand value Nm (0.0625)" in file_contents or not "1. Velocity RPM (1)" in file_contents):
            st.error("Error: torque_demand_value Data Not Found")
        else:
            # Creating torque_demand_value chart
            torque_demand_value_chart = st.line_chart(data=file_contents, x="1. Velocity RPM (1)", y="1. Torque demand value Nm (0.0625)", x_label="Velocity RPM", y_label="Torque Demand Value")
#endregion Torque Demand Value

#region Torque Actual Value
def cell_motor_torque_actual_value(file_contents):
    with st.container(border=True):
        # Pass through file contents, normally selected_file_contents

        st.header("Torque Actual Value Data", text_alignment="center")
        # Check if necessary data types exist
        if(not "1. Torque actual value Nm (0.0625)" in file_contents or not "1. Velocity RPM (1)" in file_contents):
            st.error("Error: Torque Actual Value Data Not Found")
        else:
            # Creating torque_actual_value chart
            torque_actual_value_chart = st.line_chart(data=file_contents, x="1. Velocity RPM (1)", y="1. Torque actual value Nm (0.0625)", x_label="Velocity RPM", y_label="Torque Actual Value")
#endregion Torque Actual Value

#endregion Motor Data


