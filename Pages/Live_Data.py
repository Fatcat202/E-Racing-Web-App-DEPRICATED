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
import os
from cantools import database   # pip install cantools
import can                      # pip install python-can
import serial.tools.list_ports  # pip install python-can-csscan-serial
from time import gmtime, strftime
from datetime import datetime
from streamlit_autorefresh import st_autorefresh # pip install streamlit-autorefresh

st.set_page_config(layout="wide")

# Automatically rerun the Streamlit script every 0.5 seconds
# to check if any new ports have been plugged in.
st_autorefresh(interval=500, limit=None, key="port_scanner_refresh")

date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

if "data_to_csv" not in st.session_state:
    st.session_state.data_to_csv = False

if "graphs" not in st.session_state:
    st.session_state.graphs = ["Speed", "Acceleration", "Odometry"]

if "graph1" not in st.session_state:
    st.session_state.graph1 = [] 
with st.container():
    st.header("Live Data", divider=True)
    with st.expander("Live data", expanded=True):
         # page title
        st.sidebar.markdown("Live Data") # sidebar page title

        ports = [port.device for port in serial.tools.list_ports.comports()]
        port_chosen = st.selectbox("Select an uploaded file to view:", options = ["Select Option"]+ports)

        if port_chosen != "Select Option":
            with st.expander("Advanced options", expanded=False):
                options = st.multiselect(
                    "What data do you need",
                    ["Heart", "Speed", "Acceleration", "Odometry"],
                    key="graphs"
                )
                x_axis = st.multiselect(
                    "For which data do you want the x-axis to be Distance",
                    ["Heart", "Speed", "Acceleration"],
                    key="graph1"
                )                               

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
        with can.Bus(interface="csscan_serial", channel=port_chosen) as bus:
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
                    df["Distance"] = 0
                    df["Speed"] = 0
                    name = f"Trial_Data/CANmod_gps_data{date_time}.csv"
                    df.to_csv(str(name),index=False,encoding='utf-8')
                    
                        
                    # Create columns for data cells
                    # Cells listed in columns are in order of rows
                    col1, col2, col3 = column.columns(spec=3, width="stretch")
                    #region Column 1
                    with col1:
                        if "Speed" in options:
                            if "Speed" in x_axis:
                                cell_speed(df,"distance")
                            else:
                                cell_speed(df,"time")
                        else:
                            st.empty()
                
                        if "Heart" in options:
                            if "Heart" in x_axis:
                                cell_heart_rate(df,"distance" , True)
                            else:
                                cell_heart_rate(df,"time" , True)
                        else:
                            st.empty()
            
                #endregion Column 1
            
                #region Column 2
                    with col2:
                        if "Acceleration" in options:
                            if "Acceleration" in x_axis:
                                cell_acceleration(df,"distance")
                            else:
                                cell_acceleration(df,"time")
                        else:
                            st.empty()
            
                #endregion Column 2
            
                #region Column 3
                    with col3:
                        if "Odometry" in options:
                            cell_odometry(df)
                        else:
                            st.empty()
                    
                        #endregion Column 3
                    # Prints data frames
                    print(df.tail(1))
        if(st.session_state.data_to_csv == False):
            break
except Exception as exc:
    print(exc)