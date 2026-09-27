import streamlit as st          # pip install streamlit
import pandas as pd             # streamlit dependency
import numpy as np              # streamlit dependency
import pathlib as pl            # pip install pathlib

# Script used to calculate driver heart rate zone
def scr_calculate_heart_rate_zone(heart_rate=0, age=0):
    # Pass through Heart Rate and driver Age

    # Calculate max heart rate
    HRmax = 220 - age

    # Calculate percentage of HRmax
    percent_HRmax = heart_rate / HRmax

    # Calculate zone absed on percentage
    intensity_zone = "Zone not found"
    if(percent_HRmax < 0.5):
        intensity_zone = "Warning: Zone Under 1"
    elif(percent_HRmax >= 0.5 and percent_HRmax <= 0.6):
        intensity_zone = "Zone 1"
    elif(percent_HRmax >= 0.61 and percent_HRmax <= 0.7):
        intensity_zone = "Zone 2"
    elif(percent_HRmax >= 0.71 and percent_HRmax <= 0.8):
        intensity_zone = "Zone 3"
    elif(percent_HRmax >= 0.81 and percent_HRmax <= 0.9):
        intensity_zone = "Zone 4"
    elif(percent_HRmax >= 0.91 and percent_HRmax <= 1.0):
        intensity_zone = "Zone 5"
    elif(percent_HRmax > 1.0):
        intensity_zone = "Warning: Zone Over 5"
    
    # Output percentage of HRmax
    return percent_HRmax, intensity_zone
  
  
# Script used to create a line chart
def scr_line_chart(file_name = "", x_title = "", y_title = ""):
    # Pass through file_name as string
    # Pass through X and Y axis titles as strings

    # Check file_name was passed through
    if(not pl.Path.is_file(file_name)): return st.error("Error: File name not found")
    

    x = [] # where the csv data of one coloumn of the chart goes 
    y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

    df = pd.read_csv(file_name)
    st.line_chart(df, x = x_title, y = y_title) # create the chart and assign the chart axis with the right headings #
