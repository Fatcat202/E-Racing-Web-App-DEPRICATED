import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
from Scripts import scr_line_chart



#Page used to display live data

#region Page Titles

# Display title
st.header("Live Data", divider=True)
# Display sidebar title
st.sidebar.markdown("Live Data")

#endregion Page Titles


#region Variables

# File holding heart rate data
heart_rate_data = None

#  File holding left front suspension data
lf_suspension_data = None

#  File holding left front suspension data
rf_suspension_data = None

#  File holding left front suspension data
lr_suspension_data = None

#  File holding left front suspension data
rr_suspension_data = None

# File holding motor data
motor_data = None

# File holding HV battery data
hv_battery_data = None

# File holding LV battery data
lv_battery_data = None

# File holding aero data
aero_data = None

# File holding speed data
speed_data = None

# File holding attitude data
attitude_data = None

# File holding odometer data
odometer_data = None

# File holding acceleration data
acceleration_data = None

# File holding angular data
angular_data = None

# File holding vibration data
vibration_data = None


#endregion Variables

#region Data Visualizer

#region Heart Rate

with st.expander("Heart Rate Data"):
    if(heart_rate_data == None):
        st.error("Error: Heart Rate Data Not Found")

    else:
    
        st.download_button(
            label="Download Heart rate data as excel csv file",
            data=heart_rate_data.to_csv(index=False)
         )
        scr_line_chart("Trial_Data/data.csv", "aa", "ab")
        #TODO: implement heart rate data graphs

#endregion Heart Rate

#region Suspension

with st.expander("Left Suspension Data"):

    #Left Front Suspension
    if(lf_suspension_data == None):
        st.error("Error: LF Suspension Data Not Found")
#    else:
        #TODO: implement left front data graph

with st.expander("Right Suspension Data"):
   
    #Right Front Suspension
    if(rf_suspension_data == None):
        st.error("Error: RF Suspension Data Not Found")
#    else:
        #TODO: implement right front data graph

with st.expander("Left Rear Suspension Data"):
    #Left Rear Suspension
    if(lr_suspension_data == None):
        st.error("Error: LR Suspension Data Not Found")
#    else:
    #TODO: implement left rear data graph

with st.expander("Right Rear Suspension Data"):
    #Right Rear Suspension
    if(rr_suspension_data == None):
        st.error("Error: RR Suspension Data Not Found")
#    else:
        #TODO: implement right rear data graph

#endregion Suspension
        
#region Motor

with st.expander("Motor Data"):
    if(motor_data == None):
        st.error("Error: Motor Data Not Found")
 #   else:
        #TODO: implement motor data graphs

#endregion Motor

#region HV Battery

with st.expander("HV Battery Data"):
    if(hv_battery_data == None):
        st.error("Error: HV Battery Data Not Found")
 #   else:
        #TODO: implement HV battery data graphs

#endregion HV Battery

#region LV Battery

with st.expander("LV Battery Data"):
    if(lv_battery_data == None):
        st.error("Error: LV Battery Data Not Found")
 #   else:
        #TODO: implement LV battery data graphs

#endregion LV Battery

#region Aero Data

with st.expander("Aero Data"):
    if(aero_data == None):
        st.error("Error: Aero Data Not Found")
  #  else:
        #TODO: implement Aero data graphs

#endregion Aero Data

#region Speed

# Gathered from CAN
with st.expander("Speed Data"):
    if(speed_data == None):
        st.error("Error: Speed Data Not Found")
 #   else:
        #TODO: implement Speed data graphs

#endregion Speed

#region Attitude

# Gathered from CAN
with st.expander("Attitude Data"):
    if(attitude_data == None):
        st.error("Error: Attitude Data Not Found")
 #   else:
        #TODO: implement Attitude data graphs

#endregion Attitude

#region Odometer

# Gathered from CAN
with st.expander("Odometer Data"):
    if(odometer_data == None):
        st.error("Error: Odometer Data Not Found")
    #else:
        #TODO: implement Odometer data graphs

#endregion Odometer

#region Acceleration

# Gathered from CAN
with st.expander("Acceleration Data"):
    if(acceleration_data == None):
        st.error("Error: Acceleration Data Not Found")
 #   else:
    #TODO: implement Acceleration data graphs (mohammed-done)

#endregion Acceleration

#region Angular Data

# Gathered from CAN
with st.expander("Angular Data"):
 if(angular_data == None):
        st.error("Error: Angular Data Not Found")
# else:
    #TODO: implement Angular data graphs

#endregion Angular Data

#region Vibration Data

with st.expander("Vibration Data"):
 if(vibration_data == None):
        st.error("Error: Vibration Data Not Found")
# else:
     #TODO: implement Vibration data graphs

#endregion Vibration Data


#endregion Data Visualizer



