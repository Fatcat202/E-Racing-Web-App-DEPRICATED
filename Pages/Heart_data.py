import streamlit as st          #pip install streamlit
import requests                 #pip install requests
import yaml                     #pip install pyyaml
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')


#Page used to display information shown to driver in dash

# Display title
st.header("Driver Dash", divider=True)

# Display sidebar title
st.sidebar.markdown("Heart_data")

# Page Configuration
st.set_page_config(layout="wide")

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

access_token = config["access_token"]

headers = {'Accept': 'application/json',  'Authorization': f'Bearer {access_token}'};

r = requests.get(f'https://www.polaraccesslink.com/v3/users/continuous-heart-rate/{date}', headers = headers)

if r.status_code >= 200 and r.status_code < 400:
    st.write(r.json())
else:
    st.write(r)

