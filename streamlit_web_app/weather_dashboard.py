import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# I set the page title
st.title("Global Weather Data Dashboard")

# # I allow the user to choose the data refresh frequency
refresh_rate = st.selectbox("Choose how often to refresh (seconds)", options=[1, 2, 5, 10], index=2)

# I load cleaned weather datast.header("Cleaned Weather Data")
@st.cache_data
def load_data():
    response = requests.get("http://157.230.103.203:5000/data")  # Server IP
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error("Oops! Couldn't load the cleaned data.")
        return pd.DataFrame()

data = load_data()
st.write("Here's the cleaned weather data:")
st.dataframe(data)

# # Displaying live weather updates
st.header("Live Weather Updates")
st.write("Real-time weather data coming through Kafka")

def get_live_data():
    response = requests.get("http://157.230.103.203:5000/live")  # Use the server IP
    if response.status_code == 200:
        live_data = response.json()
        return pd.DataFrame(live_data)
    else:
        st.error("Hmm, couldn't fetch the live data.")
        return pd.DataFrame()

# Data refresh process
def refresh_data():
    live_data = get_live_data()
    if not live_data.empty:
        st.write("Here are the latest 5 updates:")
        st.dataframe(live_data)
        fig = px.line(live_data, x="last_updated", y="temperature", title="Real-time Temperature Change")
        st.plotly_chart(fig)
    else:
        st.write("Looks like there's no live data right now.")

# Enable automatic page refresh
count = st_autorefresh(interval=refresh_rate * 1000, key="datarefresh")
refresh_data()
