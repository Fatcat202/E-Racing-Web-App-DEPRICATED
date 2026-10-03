import os
from cantools import ct 
import pandas as pd
import can
import streamlit as st 

# Open bus
#Change the Channel number

# locate the dbc file because it contains decoding instructions 
dbc_path = os.path.join("dbc", "canmod-gps.dbc")

# Some DBC files contain overlapping signal names like strict=False keeps the database usable for decoding.
if not os.path.exists(dbc_path): # does file exist in the location
    raise FileNotFoundError(f"DBC file not found: {dbc_path}") # if doesnt exist say doesnt exist here

db = ct.load_file(dbc_path, strict=False) # dbc file is a dictionary for raw CAN data, this uses cantools to read the dbc and know how to decode
rows = [] # starts a list to store decoded CAN frames


class CANdecoder: # class for decoding 
    def __init__(self, dbc_file): # automatically running method for decoding object
        self.db = ct.load_file(dbc_file, strict=False) # stores dbc in object for method to run automatically
    def decode(self, msg): # method for receiving raw CAN data 
        try:
            db_msg = self.db.get_message_by_frame_id(msg.arbitration_id) # msg.arbitration_id is for matching CAN frame id to dbc id to interpret it 
        except KeyError: # what if the CAN frame has no matching dbc
            return None # skip that message without stopping

        try:
            result = self.db.decode_message(db_msg.name, data=msg.data) # 
        except Exception: # what if it cant be decoded
            return None # skip and continue 

        result["t"] = msg.timestamp
        result["message_name"] = db_msg.name
        return result, db_msg

    # returns the data frame
    def data_frame(self, data):
        if data is None:
            return None

        #result, db_msg = data
        #IMPORTANT_MESSAGES = [
         #   "GnssSpeed",
          #  "GnssAttitude",
           # "GnssPosition",
            #"GnssAltitude",
         #    "GnssOdo",
          #  "GnssStatus",
           # "GnssTime",
            #"GnssImu",
         #   "GnssGeofence"
        #]
       #if db_msg.name not in IMPORTANT_MESSAGES:
      #      return None

        #return pd.DataFrame([result])

# connect to the CANmod.gps device
try:
    with can.Bus(interface="csscan_serial", channel="COM13") as bus: # what port and serial will the device be connected to
        # continuously listen for incoming frames (messages)
        canmod_gps = CANdecoder(dbc_path) # decoding object
        for msg in bus:
            decoded = canmod_gps.decode(msg)
            if decoded is not None:
                result, db_msg = decoded
                rows.append(result)

                # Save decoded data to CSV as it arrives
                df = pd.DataFrame(rows)
                df.to_csv("CANmod_gps_data.csv",index=False,encoding='utf-8')
                st.header("CAN data", divider=True) # page title
                st.sidebar.markdown("Digital Twin") # sidebar page title

                # Prints data frames
                print(df.tail(1))
except Exception as exc:
    print(exc)