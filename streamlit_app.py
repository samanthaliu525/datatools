import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Tools Dashboard")
st.write("Explore the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

if st.button('United States's Graph'):
    st.image('https://raw.githubusercontent.com/samanthaliu525/datatools/05019b5d28930c546e6d3e7f9e5e4cc70a822ec9/images/CO2_temp_US_scaled.png')

if st.button('China's Graph'):
    st.image('https://raw.githubusercontent.com/samanthaliu525/datatools/f33a4475b5df43e25839cbf0a420960f32f3bc8e/images/CO2_temp_China_scaled.png')
