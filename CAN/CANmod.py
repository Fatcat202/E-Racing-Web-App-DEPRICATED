import os # pip install os
from cantools import database # pip install cantools
import time # pip install time 
import pandas as pd 
import can # pip install can
import streamlit as st # pip install streamlit
import serial.tools.list_ports # pip install pyserial (visit this for mre on pyserial (https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.list_ports)and(https://www.pyserial.com/docs/api-reference))
# pip install python-can-csscan-serial for interface

st.header("CAN data", divider=True) # page title
st.sidebar.markdown("CAN") # sidebar page title


portl = serial.tools.list_ports.comports() # what COM ports does this device have 

available_ports = [port.device for port in portl # a filter to keep only available ports (connected ports)
    if "USB" in port.description # keep only available ports with description USB to keep only USB ports
    ]
COM_port = st.selectbox("Select an uploaded file to view:", options = ["Select Option"]+ available_ports) # selection interface and available ports to choose from
if not available_ports:
    st.error ("No COM ports are currently connected") # if no ports are connected to computer display this 
elif COM_port == "Select Option":
    st.success ("please choose a COM port") # select a port from the available ports
else:
    st.success ("Port "+COM_port+" Selected") # if you select a port it will say port selected

Important_messages = {
    "speed": ("speed"),
    "IMU": ("AccelerationX", "AngularRateX"),
    "odometer": ("DistanceTotal"),
    "time": ("Epoch"),
    "position": ("Latitude", "Longitude"),
    "information": ("Satellites")
}

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



# region optional filter 

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


#end region optional filter

# connect to the CANmod.gps device
try:
    placeholderdf = st.empty() # creates a space on the page that can be updated with new data
    with can.Bus(interface="csscan_serial", channel=COM_port) as bus:  # COM port and interface between CAN and PC
        refresh_interval = 1  # how many seconds to wait between table updates
        last_refresh = time.monotonic() # records the time of the last table update

        # continuously listen for incoming frames (messages)
        canmod_gps = CANdecoder(dbc_path)  # decode file in dbc_path
        for msg in bus:
            decoded = canmod_gps.decode(msg)
            if decoded is not None:
                result, db_msg = decoded
                rows.append(result)

            now = time.monotonic()
            if now - last_refresh >= refresh_interval:
                if rows:
                    df = pd.DataFrame(rows[-1000:]) # keeps the table to the latest 1000 decoded messages
                    placeholderdf.dataframe(df, use_container_width=True) # updates the table in the placeholder
                last_refresh = now # starts timing until the next table update

    if rows: # checks that at least one message was decoded before saving
        df = pd.DataFrame(rows[-1000:]) # prepares the latest 1000 decoded messages for saving
        df.to_csv(os.path.join("Trial_Data", "canmod_gps_data.csv"), index=False, encoding="utf-8") # creates the CSV if it does not exist, then saves the data after the listener stops
        #filtered_Important_messages = {
        #   "speed",
        #   "AccelerationX",
        #   "AngularRateX",
        #   "DistanceTotal"
        #}

    # filtered_df = df[filtered_Important_messages]
    # col1, col2, col3, col4 = st.columns(4)

    # col1.metric("speed", filtered_df["speed"])#.iloc[-10]
    # col2.metric("Acceleration", filtered_df["AccelerationX"])#.iloc[-10]
    # col3.metric("Angular Velocity", filtered_df["AngularRateX"])#.iloc[-10]
    # col4.metric("Distance Travelled", filtered_df["DistanceTotal"])#.iloc[-10]

        #Prints data frame (filtered_df) from last row (tail)
        print(df.tail(1))
        #placeholder1=st.empty()
        #placeholder1.metric(col1)
        #st.write(col1)
        #f"{col1:.1f}"
except Exception as exc:
    print(exc)