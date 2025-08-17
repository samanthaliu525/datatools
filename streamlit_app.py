import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Tools Dashboard")
st.write("Explore the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

st.subheader("CO2 World Emissions")
st.write("This is the overall world's CO2 emissions from 1751-2014. We can see the great increase in emission levels as the world became more industrialized. Note that this is limited to the countries that report their data.")
st.image("https://raw.githubusercontent.com/samanthaliu525/datatools/35db4e3e1df941e2333d0c21315c6279df0fa90c/images/CO2_world.png")

st.subheader("CO2 Emissions Tile Plot")
st.write("Let's take a look at our top 10 emittors in 2014, and how their emission levels progressed overtime. The labels of the countries go from the highest emittor in 2014 and descends.")
st.image("https://raw.githubusercontent.com/samanthaliu525/datatools/35db4e3e1df941e2333d0c21315c6279df0fa90c/images/CO2_tile.png")


st.subheader("US vs. China with different graphs")
st.write("Choose which graphs you want to see that are specific to the US or China. Most of the graphs are comparing emissions and temperature, but the last two dropdown items are looking at natural disasters, GDP, and energy usage.")
# Define the URLs for your pre-rendered PNG files on GitHub.
CO2_temp_US_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/05019b5d28930c546e6d3e7f9e5e4cc70a822ec9/images/CO2_temp_US_scaled.png"
CO2_temp_US_facet_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/14edbf5fd5a7a10e6439859214b7b11cffdf4766/images/CO2_temp_US_facet.png"
CO2_temp_China_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/f33a4475b5df43e25839cbf0a420960f32f3bc8e/images/CO2_temp_China_scaled.png"
CO2_temp_China_facet_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/8c94c7c43a14d595c92ecaaa56b4f172809653d3/images/CO2_temp_China_facet%20(1).png"
CO2_temp_China_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/1e94ffab0bc46b03d796b814f10bd82fc80fd299/images/CO2_temp_China.png"
CO2_temp_US_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/c356f4e5f29b367949fb6ec2837dcf4091f8c948/images/CO2_temp_US.png"
China_facet_plot_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/c356f4e5f29b367949fb6ec2837dcf4091f8c948/images/China_facet_plot.png"
US_facet_plot_url = "https://raw.githubusercontent.com/samanthaliu525/datatools/c356f4e5f29b367949fb6ec2837dcf4091f8c948/images/US_facet_plot.png"


# Create a selectbox (dropdown menu) to choose the plot to display
chart_options = [
    "US Scaled",
    "China Scaled",
    "US Facet",
    "China Facet",
    "CO2 vs. Temp China",
    "CO2 vs. Temp US",
    "China Facet Plot",
    "US Facet Plot"
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
elif selected_chart == "CO2 vs. Temp China":
    st.image(CO2_temp_China_url, caption="CO2 vs. Temperature for China")
elif selected_chart == "CO2 vs. Temp US":
    st.image(CO2_temp_US_url, caption="CO2 vs. Temperature for US")
elif selected_chart == "China Facet Plot":
    st.image(China_facet_plot_url, caption="China Facet Plot")
elif selected_chart == "US Facet Plot":
    st.image(US_facet_plot_url, caption="US Facet Plot")


st.subheader("Summary Plots")
if st.button("United States Summary"):
    st.write("By looking at the graphs, we can tell that the US has remained one of the highest emitting country, which we can see clearly from the tile plot. It was the highest out of the top ten countries in 2014, but China in the past fifty years has surpassed the US. From outside knowledge, we know that is correlated with their growing GDP and becoming an increasingly developed nation. There is some correlation between more CO2 emissions and temperature, but we cannot determine if it's causually correlated. It does seem like CO2 emissions in the US are associated with higher temperatures and more natural disasters since the temperatures and disasters graphs have been increasing—at least in the past 50 years since we don't have all the data before then")
    st.image("https://raw.githubusercontent.com/samanthaliu525/datatools/35db4e3e1df941e2333d0c21315c6279df0fa90c/images/mainplot_combined.png")

if st.button("China's Summary"):
    st.write("By looking at these graphs, we can see that the overall CO2 emissions have increased over the years. There are some countries that rapdily increased their emissions, like China, while others—mainly the developed countries—have remained a high emittor throughout the time period.")
    st.image("https://raw.githubusercontent.com/samanthaliu525/datatools/5cc3bd8a20a55a9f1c77c874bfcb34d357d847a6/images/China_mainplot_combined.png")

# Extra Credit Interactive Plot
st.subheader("Extra Credit Plot")
st.write("Since China grew and became the largest emittor, let's take a closer look to see their percentage of emissions in the whole world. How much of the world's emissions comes from China?")


CO2_LONG_URL = "https://raw.githubusercontent.com/samanthaliu525/datatools/refs/heads/main/data/CO2_world_clean.csv"

@st.cache_data
def load_data():
    """
    Loads the CO2 data from the GitHub repository.
    """
    with st.spinner('Loading data from GitHub...'):
        try:
            co2_long_df = pd.read_csv(CO2_LONG_URL)
            return co2_long_df
        except Exception as e:
            st.error(f"Error loading data from GitHub: {e}")
            st.info("Creating dummy data for demonstration.")
            co2_long_df = pd.DataFrame({
                'Year': list(range(1751, 2015)),
                'Emissions': np.random.rand(264) * 1000,
                'Country': ['China'] * 264
            })
            return co2_long_df

# Load the data
CO2_long = load_data()


# --- Part 2: Building the Streamlit Dashboard UI ---
st.title("China's CO₂ Emissions as % of Global Total")
st.header("Interactive Matplotlib Plot with Slider")

# --- Part 3: Create the interactive plot logic ---
# Global yearly CO2 emissions, created from co2_long
co2_world = (CO2_long
             .groupby("Year", as_index=False)["Emissions"]
             .sum()
             .rename(columns={"Emissions": "CO2_World"}))

# China yearly CO2 emissions
co2_china = CO2_long[CO2_long["Country"] == "China"].copy()
# Merge China with world totals
co2_ratio = pd.merge(co2_china, co2_world, on="Year", how="inner")

# Compute percentage
co2_ratio["China_%_World"] = (co2_ratio["Emissions"] / co2_ratio["CO2_World"]) * 100

# Create a slider to filter the data by year
min_year = int(co2_ratio['Year'].min())
max_year = int(co2_ratio['Year'].max())

start_year, end_year = st.slider(
    "Select a year range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Filter the dataframe based on the slider's selection
filtered_df = co2_ratio[(co2_ratio["Year"] >= start_year) & (co2_ratio["Year"] <= end_year)]


# --- Part 4: Display the Matplotlib plot in Streamlit ---
# Create the Matplotlib plot using the filtered data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_df["Year"], filtered_df["China_%_World"], marker="o", label="China's Share of World CO₂")
ax.set_xlabel("Year")
ax.set_ylabel("China's % of World CO₂")
ax.set_title(f"China's CO₂ Emissions as % of Global Total ({start_year}-{end_year})")
ax.legend()
ax.grid(True)
st.pyplot(fig)
