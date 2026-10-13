import os # pip install os
from cantools import database # pip install cantools
import pandas as pd 
import can # pip install can
import streamlit as st # pip install streamlit
import serial.tools.list_ports
from time import gmtime, strftime
from datetime import datetime
from Scripts.Scripts import *
from Scripts.Cells import *


date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
ports = [port.device for port in serial.tools.list_ports.comports()]

st.session_state.data_to_csv = False 

st.header("Live Data", divider=True) # page title
st.sidebar.markdown("Live Data") # sidebar page title
port_chosen = st.selectbox("Select an uploaded file to view:", options = ["Select Option"]+ports)

    
if(port_chosen is not "Select Option"):
    print(str(st.session_state.data_to_csv)+"1")
    if st.button("Start Reading Data"):
        st.session_state.data_to_csv = True 
    if st.button("Stop Reading Data"):
        st.session_state.data_to_csv = False

# locate the dbc file for decoding instructions 
dbc_path = os.path.join("CAN", "canmod-gps.dbc")

# checking for dbc file in dbc_path
if not os.path.exists(dbc_path): 
    raise FileNotFoundError(f"DBC file not found: {dbc_path}") 

db = database.load_file(dbc_path, strict=False) # read the dbc instructions in dbc file
rows = [] # starts a list to store decoded CAN frames

# Create placeholder columns to prevent replication
column = st.empty()


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
                    
                    df['time'] = df['t'] - df.loc[0,'t']
                    df['dt'] = df["time"].diff().fillna(0)
                    df['AccelerationX'] = df['AccelerationX'] - df.loc[0,'AccelerationX']
                    df['AccelerationY'] = df['AccelerationY'] - df.loc[0,'AccelerationY']
                    df['AccelerationZ'] = df['AccelerationZ'] - df.loc[0,'AccelerationZ']
                    df['Acceleration'] = (df['AccelerationX']**2 +df['AccelerationY']**2 +df['AccelerationZ']**2)**0.5
                    name = f"Trial_Data/CANmod_gps_data{date_time}.csv"
                    df.to_csv(str(name),index=False,encoding='utf-8')
                    
                        
                    # Create columns for data cells
                    # Cells listed in columns are in order of rows
                    col1, col2, col3 = column.columns(spec=3, width="stretch")
                
                    #region Column 1
                    with col1:
                        cell_speed(df)
                        cell_heart_rate(df, True)
            
                #endregion Column 1
            
                #region Column 2
                    with col2:
                        cell_acceleration(df)
            
                #endregion Column 2
            
                #region Column 3
                    with col3:
                        cell_odometry(df)
                    
                        #endregion Column 3
                    # Prints data frames
                    print(df.tail(1))
        if(st.session_state.data_to_csv == False):
            break
except Exception as exc:
    print(exc)