import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# Set page title and layout for improved UX
st.set_page_config(page_title="Global Weather Data Dashboard", layout="wide")
st.title("🌍 Global Weather Data Dashboard")

# Sidebar settings for user controls
st.sidebar.header("Dashboard Settings")
refresh_rate = st.sidebar.selectbox("Select Refresh Interval (seconds)", options=[1, 2, 5, 10], index=2)

# Load cleaned weather data function (cached)
@st.cache_data
def load_data():
    response = requests.get("http://157.230.103.203:5000/data")  # Update with actual server IP
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error("Failed to load cleaned weather data.")
        return pd.DataFrame()

# Initial load of the cleaned data
data = load_data()

# Sidebar for country selection with search-enabled dropdown
country_options = data['country'].unique() if not data.empty else []
selected_countries = st.sidebar.multiselect("Select countries to display:", country_options, default=country_options)

# Sidebar button to clear selection
if st.sidebar.button("Clear Selection"):
    selected_countries = []

# Live data retrieval function
def get_live_data():
    response = requests.get("http://157.230.103.203:5000/live")  # Update with actual server IP
    if response.status_code == 200:
        live_data = response.json()
        return pd.DataFrame(live_data)
    else:
        st.error("Unable to fetch live data.")
        return pd.DataFrame()

# Initialize session state to store accumulated live data for continuous plotting
if "live_data" not in st.session_state:
    st.session_state.live_data = pd.DataFrame()

# Function to update live data in session state
def update_live_data():
    new_data = get_live_data()
    if not new_data.empty:
        # Accumulate new data while filtering by selected countries
        st.session_state.live_data = pd.concat([st.session_state.live_data, new_data], ignore_index=True)
        # Filter based on selected countries
        st.session_state.live_data = st.session_state.live_data[st.session_state.live_data['country'].isin(selected_countries)]

# Automatic refresh to continuously fetch live data
st_autorefresh(interval=refresh_rate * 1000, key="data_refresh")
update_live_data()

# Display cleaned data in a collapsible section
with st.expander("View Cleaned Weather Data"):
    st.dataframe(data)

# Layout for the live graphs
st.markdown("### Live Weather Graphs")
cols = st.columns(3)

# Plot Temperature over Time for selected countries
if not st.session_state.live_data.empty:
    with cols[0]:
        fig_temp = px.line(
            st.session_state.live_data, x="last_updated", y="temperature", color="country",
            title="Temperature Over Time", labels={"temperature": "Temperature (°C)"}
        )
        fig_temp.update_layout(yaxis=dict(range=[st.session_state.live_data["temperature"].min() - 5,
                                                 st.session_state.live_data["temperature"].max() + 5]))
        st.plotly_chart(fig_temp, use_container_width=True)

    # Plot Humidity over Time for selected countries
    with cols[1]:
        fig_humidity = px.line(
            st.session_state.live_data, x="last_updated", y="humidity", color="country",
            title="Humidity Over Time", labels={"humidity": "Humidity (%)"}
        )
        fig_humidity.update_layout(yaxis=dict(range=[st.session_state.live_data["humidity"].min() - 5,
                                                     st.session_state.live_data["humidity"].max() + 5]))
        st.plotly_chart(fig_humidity, use_container_width=True)

    # Plot Temperature vs Coordinates (Latitude and Longitude)
    with cols[2]:
        fig_coords = px.scatter(
            st.session_state.live_data, x="latitude", y="longitude", size="temperature", color="country",
            title="Temperature by Location", labels={"latitude": "Latitude", "longitude": "Longitude"},
            hover_data={"temperature": True, "last_updated": True}
        )
        fig_coords.update_layout(yaxis=dict(scaleanchor="x", scaleratio=1))  # Make latitude and longitude equal scaling
        st.plotly_chart(fig_coords, use_container_width=True)
else:
    st.write("Waiting for live data...")

# Add footer or info section to give context
st.sidebar.markdown("#### About")
st.sidebar.info(
    "This dashboard provides real-time global weather data updates, displaying temperature, humidity, and location-specific "
    "temperature details. Select countries and set refresh intervals for a customized view. Data is refreshed seamlessly "
    "to ensure continuous tracking without interruptions."
)

