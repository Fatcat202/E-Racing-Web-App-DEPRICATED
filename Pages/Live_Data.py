import streamlit as st          #pip install streamlit
import pandas as pd #streamlit dependency
import numpy as np #streamlit dependency
import csv # for requesting a csv and writing data to and from it (no need to install)
import pathlib as pl # for finding that csv and opening it (no need to install)
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
# i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set

  x = [] # where the csv data of one coloumn of the chart goes 
  y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="aa", y="ab") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement heart rate data graphs (mohammed-done)

#endregion Heart Rate

#region Suspension

with st.expander("Left Suspension Data"):

    #Left Front Suspension
    if(lf_suspension_data == None):
        st.error("Error: LF Suspension Data Not Found")
    else:
# i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


     x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="ac", y="ad") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement left front data graph (mohammed-done)

with st.expander("Right Suspension Data"):
   
    #Right Front Suspension
 if(rf_suspension_data == None):
        st.error("Error: RF Suspension Data Not Found")
 else:

# i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="ae", y="af") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement right front data graph (mohammed-done)
with st.expander("Left Rear Suspension Data"):
    #Left Rear Suspension
 if(lr_suspension_data == None):
        st.error("Error: LR Suspension Data Not Found")
 else:

    # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="ag", y="ah") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement left rear data graph (mohammed-done)

with st.expander("Right Rear Suspension Data"):
    #Right Rear Suspension
 if(rr_suspension_data == None):
        st.error("Error: RR Suspension Data Not Found")
 else:
    # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="ai", y="aj") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement right rear data graph (mohammed-done)

#endregion Suspension
        
#region Motor

with st.expander("Motor Data"):
 if(motor_data == None):
        st.error("Error: Motor Data Not Found")
 else:
     # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="ak", y="al") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement motor data graphs (mohammed-done)

#endregion Motor

#region HV Battery

with st.expander("HV Battery Data"):
 if(hv_battery_data == None):
        st.error("Error: HV Battery Data Not Found")
 else:
     # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="am", y="an") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement HV battery data graphs (mohammed-done)

#endregion HV Battery

#region LV Battery

with st.expander("LV Battery Data"):
 if(lv_battery_data == None):
        st.error("Error: LV Battery Data Not Found")
 else:
   # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="ao", y="ap") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i =)
        #TODO: implement LV battery data graphs (mohammed-done)

#endregion LV Battery

#region Aero Data

with st.expander("Aero Data"):
 if(aero_data == None):
        st.error("Error: Aero Data Not Found")
 else:
     # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="aq", y="ar") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement Aero data graphs (mohammed-done)

#endregion Aero Data

#region Speed

# Gathered from CAN
with st.expander("Speed Data"):
 if(speed_data == None):
        st.error("Error: Speed Data Not Found")
 else:
     # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="as", y="at") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement Speed data graphs (mohammed-done)

#endregion Speed

#region Attitude

# Gathered from CAN
with st.expander("Attitude Data"):
 if(attitude_data == None):
        st.error("Error: Attitude Data Not Found")
 else:
     # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="au", y="av") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement Attitude data graphs (mohammed-done)

#endregion Attitude

#region Odometer

# Gathered from CAN
with st.expander("Odometer Data"):
 if(odometer_data == None):
        st.error("Error: Odometer Data Not Found")
 else:
 # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="aw", y="ax") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement Odometer data graphs (mohammed-done)

#endregion Odometer

#region Acceleration

# Gathered from CAN
with st.expander("Acceleration Data"):
 if(acceleration_data == None):
        st.error("Error: Acceleration Data Not Found")
 else:
 # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="ay", y="az") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement Acceleration data graphs (mohammed-done)

#endregion Acceleration

#region Angular Data

# Gathered from CAN
with st.expander("Angular Data"):
 if(angular_data == None):
        st.error("Error: Angular Data Not Found")
 else:
 # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="aaa", y="aab") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement Angular data graphs (mohammed-done)

#endregion Angular Data

#region Vibration Data

with st.expander("Vibration Data"):
 if(vibration_data == None):
        st.error("Error: Vibration Data Not Found")
 else:
 # i or identity will be the id set for each monitoring device
# this is so we can easily extract information from dataset 
# a map of all identities will be pushed on git as soon as all identities are set


  x = [] # where the csv data of one coloumn of the chart goes 
y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

pl.Path(__file__).parent / "data.csv" # find the file (change the file name inside "" whatever the dataset file name will be)
df = pd.read_csv( # open the file and read contents
    r"C:\Users\testuser\OneDrive\Documenti\attempt\data.csv" #the file address (change to new data set address)
)
st.line_chart(df, x="aac", y="aad") # create the chart and assign the chart axis with the right headings (write the two column headers in the "" after i01 or i02 =)
        #TODO: implement Vibration data graphs (mohammed-done)

#endregion Vibration Data


#endregion Data Visualizer



