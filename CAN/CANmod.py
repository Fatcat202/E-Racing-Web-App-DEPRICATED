import os # pip install os
from cantools import database # pip install cantools
import pandas as pd 
import can # pip install can
import streamlit as st # pip install streamlit
import serial.tools.list_ports

ports = [port.device for port in serial.tools.list_ports.comports()]

data_to_csv = False 

st.header("CAN data", divider=True) # page title
st.sidebar.markdown("Digital Twin") # sidebar page title
port_chosen = st.selectbox("Select an uploaded file to view:", options = ["Select Option"]+ports)

if(port_chosen is not "Select Option"):
    print(str(data_to_csv)+"1")
    if st.button("Start reading data"):
        data_to_csv = True 
    if st.button("stop reading data"):
        data_to_csv = False
    print(str(data_to_csv)+"2")

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
        result["ls /dev/ttyACM* or ls /dev/ttyUSB*message_name"] = db_msg.name # add decoded message name in result
        return result, db_msg

    # returns the data frame
    def data_frame(self, data):
        if data is None:
            return None


# connect to the CANmod.gps device
try:
    if(data_to_csv == True):
        with can.Bus(interface="csscan_serial", channel=str(port_chosen)) as bus: # COM port and interface between CAN and PC

            # continuously listen for incoming frames (messages)
            
            canmod_gps = CANdecoder(dbc_path) # decode file in dbc_path
            print(str(data_to_csv)+"3")
            for msg in bus:
                
                if(data_to_csv == False): break
                print(str(data_to_csv)+"4")
                decoded = canmod_gps.decode(msg)
                if decoded is not None:
                    result, db_msg = decoded
                    rows.append(result)
                    # save decoded data and send it to Trial_Data as csv 
                    df = pd.DataFrame(rows)
                    df.to_csv(os.path.join ("Trial_Data", "canmod_gps_data.csv"), index=False, encoding="utf-8")
                    # Prints data frame (df) from last row (tail)
                    #print(df.tail(1))
    else:
        bus.close()
except Exception as exc:
    print(exc)