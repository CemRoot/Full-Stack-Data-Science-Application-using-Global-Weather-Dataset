import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# Set page title and layout
st.set_page_config(page_title="Real-Time Weather Dashboard", layout="wide")

# Main title
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🌍 Real-Time Global Weather Dashboard</h1>", unsafe_allow_html=True)

# Sidebar - Configuration and filters
st.sidebar.header("Settings")
st.sidebar.write("Customize your view")

# Refresh rate selection
refresh_rate = st.sidebar.selectbox("Refresh Interval (seconds)", options=[1, 2, 5, 10], index=2)

# Load initial weather data function (static for reference)
@st.cache_data
def load_initial_data():
    response = requests.get("http://157.230.103.203:5000/data")  # Use your server IP
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.sidebar.error("Failed to load initial data.")
        return pd.DataFrame()

initial_data = load_initial_data()
available_countries = initial_data['country'].unique() if not initial_data.empty else []

# Sidebar - Country selector with search option
selected_countries = st.sidebar.multiselect("Choose countries", available_countries, default=available_countries[:5])

# Sidebar - Graph selector
st.sidebar.subheader("Graphs to Display")
show_temp = st.sidebar.checkbox("Temperature over Time", value=True)
show_humidity = st.sidebar.checkbox("Humidity over Time", value=True)
show_location_temp = st.sidebar.checkbox("Temperature by Location", value=True)

# Initialize session state for accumulating live data
if "live_data" not in st.session_state:
    st.session_state.live_data = pd.DataFrame()

# Function to fetch live data from API
def fetch_live_data():
    response = requests.get("http://157.230.103.203:5000/live")  # Replace with actual server IP
    if response.status_code == 200:
        live_data = pd.DataFrame(response.json())
        return live_data[live_data['country'].isin(selected_countries)]  # Filter by selected countries
    else:
        st.error("Unable to retrieve live data.")
        return pd.DataFrame()

# Update live data in session state
def update_live_data():
    new_data = fetch_live_data()
    if not new_data.empty:
        st.session_state.live_data = pd.concat([st.session_state.live_data, new_data]).drop_duplicates().reset_index(drop=True)

# Automatic refresh
st_autorefresh(interval=refresh_rate * 1000, key="data_refresh")
update_live_data()

# Dashboard layout
st.markdown("## Live Weather Graphs")
cols = st.columns(3)

# Display Temperature over Time if selected
if show_temp and not st.session_state.live_data.empty:
    with cols[0]:
        temp_fig = px.line(st.session_state.live_data, x="last_updated", y="temperature", color="country",
                           title="Temperature Over Time", labels={"temperature": "Temperature (°C)", "last_updated": "Time"})
        temp_fig.update_traces(mode="lines+markers")
        st.plotly_chart(temp_fig, use_container_width=True)

# Display Humidity over Time if selected, with check for humidity column
if show_humidity and not st.session_state.live_data.empty:
    if "humidity" in st.session_state.live_data.columns:
        with cols[1]:
            humidity_fig = px.line(
                st.session_state.live_data, x="last_updated", y="humidity", color="country",
                title="Humidity Over Time", labels={"humidity": "Humidity (%)", "last_updated": "Time"}
            )
            humidity_fig.update_traces(mode="lines+markers")
            st.plotly_chart(humidity_fig, use_container_width=True)
    else:
        with cols[1]:
            st.warning("Humidity data is not available in the current dataset.")

# Display Temperature by Location if selected
if show_location_temp and not st.session_state.live_data.empty:
    with cols[2]:
        loc_temp_fig = px.scatter_geo(
            st.session_state.live_data,
            lat="latitude",
            lon="longitude",
            color="temperature",
            size="temperature",
            hover_name="country",
            projection="natural earth",
            title="Temperature by Location",
            labels={"temperature": "Temperature (°C)"}
        )
        loc_temp_fig.update_geos(showcoastlines=True, coastlinecolor="LightBlue", showland=True, landcolor="LightGreen")
        st.plotly_chart(loc_temp_fig, use_container_width=True)

# Footer for additional info
st.sidebar.markdown("### About")
st.sidebar.info(
    """
    This real-time weather dashboard allows you to view temperature and humidity updates across the world.
    You can select specific countries, choose the graphs to display, and set the refresh rate for data updates.
    """
)

# Styling tips and color consistency for improved UX
st.markdown(
    """
    <style>
    .css-1offfwp, .css-1inwz65, .css-1d391kg {
        background-color: #f5f5f5 !important;
    }
    .st-bp {
        color: #4A90E2 !important;
    }
    </style>
    """, unsafe_allow_html=True
)
