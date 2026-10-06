import os # pip install os
from cantools import database # pip install cantools
import pandas as pd 
import can # pip install can
import streamlit as st # pip install streamlit
import serial.tools.list_ports
from time import sleep

ports = [port.device for port in serial.tools.list_ports.comports()]

st.session_state.data_to_csv = False 

st.header("CAN data", divider=True) # page title
st.sidebar.markdown("Digital Twin") # sidebar page title
port_chosen = st.selectbox("Select an uploaded file to view:", options = ["Select Option"]+ports)

    
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

# 
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
                    df.to_csv("Trial_Data/CANmod_gps_data.csv",index=False,encoding='utf-8')
                    # Prints data frames
                    print(df.tail(1))
        if(st.session_state.data_to_csv == False):
            break
except Exception as exc:
    print(exc)