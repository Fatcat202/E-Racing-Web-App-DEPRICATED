import streamlit as st          #pip install streamlit

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





