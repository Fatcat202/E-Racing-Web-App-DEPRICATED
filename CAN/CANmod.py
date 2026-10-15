from __future__ import absolute_import

import os # pip install os
from cantools import database # pip install cantools
import time # pip install time 
import pandas as pd 
import can # pip install can
import streamlit as st # pip install streamlit
import serial.tools.list_ports # pip install pyserial (visit this for mre on pyserial (https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.list_ports)and(https://www.pyserial.com/docs/api-reference))
import sys
# pip install python-can-csscan-serial for interface

import glob
import os
from serial.tools import list_ports_common

st.header("CAN data", divider=True) # page title
st.sidebar.markdown("CAN") # sidebar page title


#Important_messages = {
 #   "speed": ("speed"),
  #  "IMU": ("AccelerationX", "AngularRateX"),
   # "odometer": ("DistanceTotal"),
    #"time": ("Epoch"),
#    "position": ("Latitude", "Longitude"),
 #   "information": ("Satellites")
#}

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

# region linux serial port
class SysFS(list_ports_common.ListPortInfo):
    """Wrapper for easy sysfs access and device info"""

    def __init__(self, device):
        super(SysFS, self).__init__(device)
        # special handling for links
        if device is not None and os.path.islink(device):
            device = os.path.realpath(device)
            is_link = True
        else:
            is_link = False
        self.usb_device_path = None
        if os.path.exists('/sys/class/tty/{}/device'.format(self.name)):
            self.device_path = os.path.realpath('/sys/class/tty/{}/device'.format(self.name))
            self.subsystem = os.path.basename(os.path.realpath(os.path.join(self.device_path, 'subsystem')))
            
        else:
            self.device_path = None
            self.subsystem = None
        # check device type
        if self.subsystem == 'usb-serial':
            self.usb_interface_path = os.path.dirname(self.device_path)
        elif self.subsystem == 'usb':
            self.usb_interface_path = self.device_path
        else:
            self.usb_interface_path = None
        # fill-in info for USB devices
        if self.usb_interface_path is not None:
            self.usb_device_path = os.path.dirname(self.usb_interface_path)

            try:
                num_if = int(self.read_line(self.usb_device_path, 'bNumInterfaces'))
            except ValueError:
                num_if = 1

            self.vid = int(self.read_line(self.usb_device_path, 'idVendor'), 16)
            self.pid = int(self.read_line(self.usb_device_path, 'idProduct'), 16)
            self.serial_number = self.read_line(self.usb_device_path, 'serial')
            if num_if > 1:  # multi interface devices like FT4232
                self.location = os.path.basename(self.usb_interface_path)
            else:
                self.location = os.path.basename(self.usb_device_path)

            self.manufacturer = self.read_line(self.usb_device_path, 'manufacturer')
            self.product = self.read_line(self.usb_device_path, 'product')
            self.interface = self.read_line(self.usb_interface_path, 'interface')

        if self.subsystem in ('usb', 'usb-serial'):
            self.description = self.usb_description()
            self.hwid = self.usb_info()

        #~ elif self.subsystem in ('pnp', 'amba'):  # PCI based devices, raspi
        elif self.subsystem == 'pnp':  # PCI based devices
            self.description = self.name
            self.hwid = self.read_line(self.device_path, 'id')
        elif self.subsystem == 'amba':  # raspi
            self.description = self.name
            self.hwid = os.path.basename(self.device_path)

        if is_link:
            self.hwid += ' LINK={}'.format(device)

    def read_line(self, *args):
        """\
        Helper function to read a single line from a file.
        One or more parameters are allowed, they are joined with os.path.join.
        Returns None on errors..
        """
        try:
            with open(os.path.join(*args)) as f:
                line = f.readline().strip()
            return line
        except IOError:
            return None


def comports(include_links=False, hide_subsystems=[]):
    devices = set()
    with open('/proc/tty/drivers') as drivers:
        for driver in drivers.readlines():
            items = driver.strip().split()
            if items[4] == 'serial':
                devices.update(glob.glob(items[1]+'*'))

    if include_links:
        devices.update(list_ports_common.list_links(devices))
    return [info
            for info in [SysFS(d) for d in devices]
            if info.subsystem not in hide_subsystems]

# gather standard USB ports on all platforms and add the Linux serial devices
# discovered from sysfs so both appear in the same selector.
portl = serial.tools.list_ports.comports()
available_ports = [
    port.device
    for port in portl
    if "USB" in (port.description or "")
]
if sys.platform.startswith("linux"):
    available_ports.extend(port.device for port in comports())
available_ports = list(dict.fromkeys(available_ports))

with st.expander("Available serial ports"):
    COM_port = st.selectbox(
        "Select a serial port:",
        options=["Select Option"] + available_ports,
    )
    if not available_ports:
        st.error("No COM ports are currently connected")
    elif COM_port == "Select Option":
        st.success("Please choose a COM port")
    else:
        st.success("Port " + COM_port + " selected")

# connect to the CANmod.gps device
try:
    placeholderdf = st.empty() # creates a space on the page that can be updated with new data
    with can.Bus(interface="csscan_serial", channel=COM_port) as bus:  # COM port and interface between CAN and PC
        refresh_interval = 1  # how many seconds to wait between table updates
        last_refresh = time.monotonic() # records the time of the last table update
except Exception as exc:
    print(exc)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# test
if __name__ == '__main__':
    for info in sorted(comports()):
        print("{0}: {0.subsystem}".format(info))
# end region linux serial port 
       