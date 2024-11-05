import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Set page title and layout
st.set_page_config(page_title="Real-Time Weather Dashboard", layout="wide")

# Main title
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🌍 Real-Time Global Weather Dashboard</h1>",
            unsafe_allow_html=True)

# Sidebar - Configuration and filters
st.sidebar.header("Settings")
st.sidebar.write("Customize your view")


# Load initial weather data
@st.cache_data
def load_initial_data():
    response = requests.get("http://157.230.103.203:5000/data")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.sidebar.error("Failed to load initial data.")
        return pd.DataFrame()


initial_data = load_initial_data()
available_countries = initial_data['country'].unique() if not initial_data.empty else []

# Sidebar - Country selector with search option and max selection
selected_countries = st.sidebar.multiselect(
    "Choose up to 5 countries", available_countries, default=available_countries[:5],
    help="You can select a maximum of 5 countries."
)


def update_available_countries():
    # Kafka'dan canlı veri çekiliyor
    live_data = fetch_live_data()
    if not live_data.empty and 'country' in live_data.columns:
        # Mevcut verideki ülkeleri dinamik olarak güncelle
        st.session_state.available_countries = live_data['country'].unique()


# Uygulama başlangıcında veya yeni veri geldiğinde güncelle
if "available_countries" not in st.session_state:
    st.session_state.available_countries = initial_data['country'].unique()
else:
    update_available_countries()

# Sidebar - Dinamik ülke seçici
selected_countries = st.sidebar.multiselect(
    "Choose up to 5 countries", st.session_state.available_countries, default=st.session_state.available_countries[:5],
    help="You can select a maximum of 5 countries."
)
if len(selected_countries) > 5:
    st.sidebar.warning("You can select up to 5 countries only.")
    selected_countries = selected_countries[:5]

# Sidebar - Graph selector
st.sidebar.subheader("Graphs to Display")
show_temp = st.sidebar.checkbox("Temperature over Time", value=True)
show_humidity = st.sidebar.checkbox("Humidity over Time", value=True)

# Initialize session state for accumulating live data
if "live_data" not in st.session_state:
    st.session_state.live_data = pd.DataFrame()


# Function to fetch live data from API
def fetch_live_data():
    response = requests.get("http://157.230.103.203:5000/live")
    if response.status_code == 200:
        live_data = pd.DataFrame(response.json())
        st.write("Fetched live data:", live_data)  # Veriyi görüntüleme
        if 'country' in live_data.columns:
            return live_data[live_data['country'].isin(selected_countries)]
        else:
            st.error("Country data not available in the response.")
            return pd.DataFrame()
    else:
        st.error("Unable to retrieve live data.")
        return pd.DataFrame()


# Update live data in session state
new_data = fetch_live_data()
if not new_data.empty:
    st.session_state.live_data = pd.concat([st.session_state.live_data, new_data]).drop_duplicates().reset_index(
        drop=True)

# Dashboard layout
st.markdown("## Live Weather Graphs")
cols = st.columns(2)

# Display Temperature over Time if selected
if show_temp and not st.session_state.live_data.empty:
    with cols[0]:
        temp_fig = px.line(st.session_state.live_data, x="last_updated", y="temperature", color="country",
                           title="Temperature Over Time",
                           labels={"temperature": "Temperature (°C)", "last_updated": "Time"})
        temp_fig.update_traces(mode="lines")
        st.plotly_chart(temp_fig, use_container_width=True)

# Display Humidity over Time if selected
if show_humidity and not st.session_state.live_data.empty:
    if "humidity" in st.session_state.live_data.columns:
        with cols[1]:
            humidity_fig = px.line(st.session_state.live_data, x="last_updated", y="humidity", color="country",
                                   title="Humidity Over Time",
                                   labels={"humidity": "Humidity (%)", "last_updated": "Time"})
            humidity_fig.update_traces(mode="lines")
            st.plotly_chart(humidity_fig, use_container_width=True)
    else:
        with cols[1]:
            st.warning("Humidity data is not available in the current dataset.")
