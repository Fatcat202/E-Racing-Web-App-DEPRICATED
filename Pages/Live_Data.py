import streamlit as st          #pip install streamlit
import pandas as pd             #streamlit dependency
import numpy as np              #streamlit dependency
import csv                      #
import pathlib as pl            # pip install pathlib
from Scripts.Scripts import scr_calculate_heart_rate_zone
from Scripts.Cells import *
import os
from cantools import database   # pip install cantools
import can                      # pip install python-can
import serial.tools.list_ports  # pip install python-can-csscan-serial
from time import gmtime, strftime
from datetime import datetime


#Page used to display live data

#region Variables

# Declares if a live connection to data is established, default false
live_connection = False

# Holds contents of file. Filled in CAN Input
file_contents = None

#endregion Variables

#region Page Titles

# Display title
st.header("Live Data", divider=True)
# Display sidebar title
st.sidebar.markdown("Live Data")

# Page Configuration
st.set_page_config(layout="wide")

#endregion Page Titles

#region CAN Input

# Find current time for filename
date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Locate all ports
ports = [port.device for port in serial.tools.list_ports.comports()]

st.session_state.data_to_csv = False 

# Allow user to select port
port_chosen = st.selectbox("Select a Port Connection to CAN:", options = ["Select Option"]+ports)

# Allow user to start and stop data connection
if(port_chosen is not "Select Option"):
    print(str(st.session_state.data_to_csv)+"1")
    if st.button("Start reading data"):
        st.session_state.data_to_csv = True 
    if st.button("stop reading data"):
        st.session_state.data_to_csv = False

# locate the dbc file for decoding instructions 
dbc_path = os.path.join("CAN", "canmod-gps.dbc")

# checking for dbc file in dbc_path
if not os.path.exists(dbc_path): 
    raise FileNotFoundError(f"DBC file not found: {dbc_path}") 

db = database.load_file(dbc_path, strict=False) # read the dbc instructions in dbc file
rows = [] # starts a list to store decoded CAN frames


class CANdecoder:  
    def __init__(self, dbc_file): # method for decoding object
        self.db = database.load_file(dbc_file, strict=False) # stores dbc_file in decoding object
    def decode(self, msg): # method for receiving raw CAN data 
        try:
            db_msg = self.db.get_message_by_frame_id(msg.arbitration_id) # matching CAN frame id to dbc id to interpret it 
        except KeyError: # what if the CAN frame has no matching dbc
            return None # skip that message without stopping
        try:
            result = self.db.decode_message(db_msg.name, data=msg.data) # decode raw data and store in result
        except Exception: # what if it cant be decoded
            return None # skip and continue 

        result["t"] = msg.timestamp # timestamping the decoded data in result
        result["message_name"] = db_msg.name # add decoded message name in result
        return result, db_msg

    # returns the data frame
    def data_frame(self, data):
        if data is None:
            return None
        
        result, db_msg = data
        return pd.DataFrame([result])

# connect to the CANmod.gps device
try:
    while (st.session_state.data_to_csv == True):
        with can.Bus(interface="csscan_serial", channel="COM5") as bus:
            # continuously listen for incoming frames (messages)
            canmod_gps = CANdecoder(dbc_path)
            for msg in bus:
                if(st.session_state.data_to_csv == False):
                            break
                
                decoded = canmod_gps.decode(msg)
                if decoded is not None:
                    result, db_msg = decoded
                    for key in list(result):
                        if "valid" in key.lower() or "accuracy" in key.lower():
                            del result[key]
                    rows.append(result)
                    # Save decoded data to CSV as it arrives
                    df = pd.DataFrame(rows)
                    dt = 0.1
                    df['time'] = df['t'] - df.loc[0,'t']
                    df['AccelerationX'] = df['AccelerationX'] - df.loc[0,'AccelerationX']
                    df['AccelerationY'] = df['AccelerationY'] - df.loc[0,'AccelerationY']
                    df['AccelerationZ'] = df['AccelerationZ'] - df.loc[0,'AccelerationZ']
                    df['Acceleration'] = (df['AccelerationX']**2 +df['AccelerationY']**2 +df['AccelerationZ']**2)**0.5
                    df['Speed'] = df['Acceleration']*dt
                    df['Distance'] = df['Speed']*dt
                    name = f"Trial_Data/CANmod_gps_data{date_time}.csv"
                    df.to_csv(str(name),index=False,encoding='utf-8')
                    # Prints data frames
                    print(df.tail(1))

                    # Update live connection to true
                    live_connection = True

                    # Store df data in file_contents
                    file_contents = df

        if(st.session_state.data_to_csv == False):

            # Update live connection to false
            live_connection = False
            break
except Exception as exc:
    # Declare connection could not be made
    print(exc)

#endregion CAN Input

#region Live Connection Display
# Widget showing if connection to live data is active
with st.sidebar:
    if live_connection is True:
        st.success("Live")
    else:
        st.error("No Data Stream")
#endregion Live Connection Display

#region Data Visualizer

# Check for valid file contents, a live connection made
if(file_contents != None and live_connection == True):

    # Create columns for data cells
    # Cells listed in columns are in order of rows
    col1, col2, col3 = st.columns(spec=3, width="stretch")

    #region Column 1
    with col1:

        cell_speed(file_contents)

        cell_heart_rate(file_contents, live_connection=live_connection)

    #endregion Column 1

    #region Column 2
    with col2:

        cell_acceleration(file_contents)

    #endregion Column 2

    #region Column 3
    with col3:

        cell_odometry(file_contents)

    #endregion Column 3

#endregion Data Visualizer

