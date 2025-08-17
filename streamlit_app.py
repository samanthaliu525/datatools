import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Tools Dashboard")
st.write("Explore the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

if st.button('United States'):
    st.write('US')

if st.button('United States Graph'):
    st.image('https://raw.githubusercontent.com/samanthaliu525/datatools/f33a4475b5df43e25839cbf0a420960f32f3bc8e/images/CO2_temp_China_scaled.png')
