import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Tools Dashboard")
st.write("Explore the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

st.subheader('Emissions and Temperature')
CO2_temp_US_facet_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/d3f902e6facd88596ae1367741663ba9119887/CO2_temp_US_facet.png"
CO2_temp_China_facet_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/588861cbce38e704a91563c9daf4281188067556/CO2_temp_China_facet%20(1).png'

# Create buttons to choose the plot to display
col1, col2 = st.columns(2)
with col1:
    show_us = st.button("United States")
with col2:
    show_china = st.button("China")

# Use a state variable to track which button was clicked last
if 'last_clicked' not in st.session_state:
    st.session_state.last_clicked = 'us'

if show_us:
    st.session_state.last_clicked = 'us'
elif show_china:
    st.session_state.last_clicked = 'china'

# Display the correct image based on the last clicked button
if st.session_state.last_clicked == 'us':
    st.image(CO2_temp_US_facet_url, caption="United States")
elif st.session_state.last_clicked == 'china':
    st.image(CO2_temp_China_facet_url, caption="China")
else: # A default plot if no button has been clicked yet.
    st.image(CO2_temp_US_facet_url, caption="United States")


st.subheader('Emissions vs. Temperature - Scaled')
CO2_temp_US_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/d3f902e6facd88596ae1367741663ba914119887/CO2_temp_US_scaled.png"
CO2_temp_China_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/37b578aaecd79f967b66478f6a56ffe878e217ee/CO2_temp_China_scaled.png"


# Create buttons to choose the plot to display
col1, col2 = st.columns(2)
with col1:
    show_us = st.button("United States")
with col2:
    show_china = st.button("China")

# Use a state variable to track which button was clicked last
if 'last_clicked' not in st.session_state:
    st.session_state.last_clicked = 'us'

if show_us:
    st.session_state.last_clicked = 'us'
elif show_china:
    st.session_state.last_clicked = 'china'

# Display the correct image based on the last clicked button
if st.session_state.last_clicked == 'us':
    st.image(CO2_temp_US_scaled_url, caption="United States")
elif st.session_state.last_clicked == 'china':
    st.image(CO2_temp_China_scaled_url, caption="China")
else: # A default plot if no button has been clicked yet.
    st.image(CO2_temp_US_scaled_url, caption="United States")
