import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Tools Dashboard")
st.write("Explore the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

# Define the URLs for your pre-rendered PNG files on GitHub.
CO2_temp_US_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/05019b5d28930c546e6d3e7f9e5e4cc70a822ec9/images/CO2_temp_US_scaled.png"
CO2_temp_US_facet_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/blob/14edbf5fd5a7a10e6439859214b7b11cffdf4766/images/CO2_temp_US_facet.png"
CO2_temp_China_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/f33a4475b5df43e25839cbf0a420960f32f3bc8e/images/CO2_temp_China_scaled.png"
CO2_temp_China_facet_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/8c94c7c43a14d595c92ecaaa56b4f172809653d3/images/CO2_temp_China_facet%20(1).png"


# Create a selectbox (dropdown menu) to choose the plot to display
chart_options = [
    "US Scaled",
    "US Facet",
    "China Scaled",
    "China Facet"
]

selected_chart = st.selectbox("Select a chart to view:", chart_options)

# Display the correct image based on the selected option
if selected_chart == "US Scaled":
    st.image(CO2_temp_US_scaled_url, caption="United States - Scaled")
elif selected_chart == "US Facet":
    st.image(CO2_temp_US_facet_url, caption="United States - Facet")
elif selected_chart == "China Scaled":
    st.image(CO2_temp_China_scaled_url, caption="China - Scaled")
elif selected_chart == "China Facet":
    st.image(CO2_temp_China_facet_url, caption="China - Facet")
