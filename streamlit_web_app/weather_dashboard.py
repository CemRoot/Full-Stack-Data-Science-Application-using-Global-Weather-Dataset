import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# Set the page title
st.title("Enhanced Global Weather Data Dashboard")

# Choose the refresh frequency
refresh_rate = st.selectbox("Choose how often to refresh (seconds)", options=[1, 2, 5, 10], index=2)

# Load cleaned weather data (cached)
@st.cache_data
def load_data():
    response = requests.get("http://157.230.103.203:5000/data")  # Replace with actual server IP
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error("Oops! Couldn't load the cleaned data.")
        return pd.DataFrame()

data = load_data()
st.write("Here's the cleaned weather data:")
st.dataframe(data)

# Initialize session state to store live data for continuous plotting
if "live_data" not in st.session_state:
    st.session_state.live_data = pd.DataFrame()

# Country selection in the sidebar for filtering live data
st.sidebar.header("Country Selection")
country_options = data['country'].unique() if not data.empty else []
selected_countries = st.sidebar.multiselect("Select countries to display:", options=country_options, default=country_options, help="Choose countries to show data for in the charts.")

# Option to clear all selections
if st.sidebar.button("Clear Selection"):
    selected_countries = []

# Fetch live data from API
def get_live_data():
    response = requests.get("http://157.230.103.203:5000/live")  # Replace with actual server IP
    if response.status_code == 200:
        live_data = response.json()
        return pd.DataFrame(live_data)
    else:
        st.error("Couldn't fetch the live data.")
        return pd.DataFrame()

# Update live data in session state for continuity
def update_live_data():
    new_data = get_live_data()
    if not new_data.empty:
        # Append new data to session_state.live_data
        st.session_state.live_data = pd.concat([st.session_state.live_data, new_data], ignore_index=True)
        # Filter by selected countries
        st.session_state.live_data = st.session_state.live_data[st.session_state.live_data['country'].isin(selected_countries)]

# Auto-refresh the page
st_autorefresh(interval=refresh_rate * 1000, key="data_refresh")

# Update live data on every refresh
update_live_data()

# Plot Temperature and Humidity over Time
if not st.session_state.live_data.empty:
    # Temperature Plot
    fig_temp = px.line(st.session_state.live_data, x="last_updated", y="temperature",
                       color="country", title="Live Temperature Updates")
    fig_temp.update_layout(yaxis_title="Temperature (°C)")
    st.plotly_chart(fig_temp, use_container_width=True)

    # Humidity Plot
    fig_humidity = px.line(st.session_state.live_data, x="last_updated", y="humidity",
                           color="country", title="Live Humidity Updates")
    fig_humidity.update_layout(yaxis_title="Humidity (%)")
    st.plotly_chart(fig_humidity, use_container_width=True)
else:
    st.write("Waiting for live data...")
