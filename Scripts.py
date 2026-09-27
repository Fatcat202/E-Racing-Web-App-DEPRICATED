import streamlit as st          # pip install streamlit
import pandas as pd             # streamlit dependency
import numpy as np              # streamlit dependency
import pathlib as pl            # pip install pathlib




def scr_line_chart(file_name = "", x_title = "", y_title = ""):
    # Pass through file_name as string
    # Pass through X and Y axis titles as strings

    # Check file_name was passed through
    if(not pl.Path.is_file(file_name)): return st.error("Error: File name not found")
    

    x = [] # where the csv data of one coloumn of the chart goes 
    y = [] # where the csv data of the other coloumn of the chart goes before it goes into the chart

    df = pd.read_csv(file_name)
    st.line_chart(df, x_title, y_title) # create the chart and assign the chart axis with the right headings #
