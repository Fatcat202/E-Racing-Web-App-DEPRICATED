import streamlit as st          #pip install streamlit

#Page used to display live data

#region Page Titles
# Display title
st.header("Welcome", divider=True)

# Display sidebar title
st.sidebar.markdown("Welcome")

#endregion Page Titles


#region Page Text

st.write("Welcome to the LJMU E-Racing team sensor data visualizer web app")

st.divider()

st.write("This application is split into three sections:")
st.write("1: Live Data - Used to view data gathered directly from the vehicle")
st.write("2: Load Data - Used to view data from a previous test run")
st.write("3: Driver Dash - View a live simulation of what the driver can see displayed on their dashboard")
st.write("4: Digital Twin - Used to create a digital twin of the vehicle")
st.write("5: Anomaly Detection - Used to detect anomalies in the vehicle")

st.divider()

#endregion Page Text


#region Implemented Sensors

# Subheader text
st.subheader("Sensors Implemented")

# Script used for easy implementation of sensors
def scr_sensor_implemented(name = "", implemented = False):
    #Pass through name of sensor as string, implemented as boolean

    _implemented = ":green-badge[Implemented]"
    _not_implemented = ":red-badge[Not Implemented]"

    if(implemented == True):
        st.markdown(name + " &mdash; " + _implemented)
    else:
        st.markdown(name + " &mdash; " + _not_implemented)
    
# Sensors
scr_sensor_implemented("Acceleration", True)
scr_sensor_implemented("Speed", False)
scr_sensor_implemented("Odometer", False)
scr_sensor_implemented("Heart Rate", False)
scr_sensor_implemented("Suspension", False)
scr_sensor_implemented("Motor", False)
scr_sensor_implemented("HV Battery", False)
scr_sensor_implemented("LV Battery", False)
scr_sensor_implemented("Aero", False)
scr_sensor_implemented("Attitude", False)
scr_sensor_implemented("Angular", False)
scr_sensor_implemented("Vibration", False)


#endregion Implemented Sensors


