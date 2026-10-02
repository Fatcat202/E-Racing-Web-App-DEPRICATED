
# LJMU E-Racing Web App

## Table of Contents
- [Rules](#RULES)
- [Features](#FEATURES)
- [Launching](#LAUNCHING)
- [Code Style Guide](#CODESTYLEGUIDE)
- [Structure](#STRUCTURE)
- [Required Software](#REQUIREDSOFTWARE)
- [Scripts](#SCRIPTS)



## RULES:
- 1: LLM Usage: Due to the safety, accuracy, performance, and maintenance requirements of our software, the use of LLMs for the creation of code will not be permitted. 
  The use of which detracts from the educational aspect of our work, and will lead to sustainability issues long-term. The extent of its use, if any, should be limited to a search function or rubber ducking. <br/>
- 2: Contributing: To contribute to the project, create your own branch from the branch listed as LIVE. From there, complete your work and create a pull request to the WORKING branch for it to be reviewed and accepted.
- 3: Sensitive Information: Sensitive information, such as personal data or passwords, should never be stored in this repository to comply with GDPR and to maintain basic security standards.



## FEATURES:
  This application is designed for the following features: <br/>
  - Displaying to the team live data from vehicle sensors by communicating with the CAN system. (Not Implemented)
  - Allowing the team to view saved data for analysis. (Not Implemented)
  - Displaying to the team a simulation of what the driver can see on their dashboard. (Not Implemented)
  - Simulating the vehicle for performance and testing. (Not Implemented)
  - Using sensor data to detect for anomalies. (Not Implemented)


# LAUNCHING:
To launch the software, use `streamlit run Main.py` in your IDE's integrated terminal.


## CODE STYLE GUIDE:
- Code is to be written in snake case: (data_file_contents, live_connection)
- Comments must be used to describe the purpose of code written so all others may understand your work. Keep comments short, but long enough to clearly describe.
- Use regions to segment code: <br/>
#region (Title of region) <br/>
  (Your code here) <br/>
#endregion (Title of region)
- Files/Folders are to be named in the style listed: (Scripts.py, Live_Data.py, Trial_Data, Images)
- Libraries used should be displayed at the top of files in the format: `#import streamlit as py      #pip install streamlit`
- Tabs, not spaces.


## STRUCTURE:
- The purpose of the Main.py file is to act as the "starting point" for the application.
- Main.py contains: <br/>
Pages <br/>
Navigation <br/>
E-Racing Logo <br/>
- Scripts.py holds frequently used scripts.
- The folder Trial_Data contains saved test run data as CSV files.
- Loading data for analysis functions as follows: Upload Data --> Select File --> View Data


# REQUIRED SOFTWARE
#### Python 3.14.7
#### Streamlit
    pip install pathlib
#### Pathlib
    pip install streamlit

## SCRIPTS:
### scr_calculate_heart_rate_zones(heart_rate, age) <br/>
#### Parameters: <br/>
- heart_rate (Integer): Pass through an integer containing the heart rate of the driver <br/>
- age (Integer): Pass through the age of the driver <br/>
#### Returns: <br/>
- percent_HRmax (Float): Percentage of driver's heart rate relative to max.<br/>
- intensity_zone (String): Heart Rate Zone the driver is in. <br/>
#### Purpose: Calculate driver heart rate zones based on active heart rate and age.
  
  


