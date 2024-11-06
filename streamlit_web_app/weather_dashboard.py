import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import time
from datetime import datetime

# Sayfa başlığı ve düzeni
st.set_page_config(page_title="🌍 Real-Time Global Weather Dashboard", layout="wide")

# Başlık ve açıklama
st.title("🌍 Real-Time Global Weather Dashboard")
st.write("Anlık sıcaklık ve nem verilerini ülke bazında görselleştirir.")

# Boş bir DataFrame oluşturma
data = pd.DataFrame(columns=['timestamp', 'country', 'temperature', 'humidity'])

# Grafik yer tutucu
placeholder = st.empty()

# Veriyi API'den düzenli olarak çekme ve görselleştirme
for _ in range(200):  # 200 güncelleme simüle ediliyor
    try:
        # API'den veri çekme
        response = requests.get("http://157.230.103.203:5000/live")
        if response.status_code == 200:
            live_data = response.json()

            for entry in live_data:
                # Yeni veri ekleme
                new_data = pd.DataFrame([[datetime.now(), entry['country'], entry['temperature'], entry['humidity']]],
                                        columns=['timestamp', 'country', 'temperature', 'humidity'])
                data = pd.concat([data, new_data], ignore_index=True).tail(100)  # Son 100 veriyi tutuyor

            # Grafikleri güncelleme
            with placeholder.container():
                fig_temp = px.line(data, x='timestamp', y='temperature', color='country',
                                   title='Real-Time Temperature by Country')
                fig_temp.update_layout(xaxis_title='Time', yaxis_title='Temperature (°C)', legend_title='Country')

                fig_humidity = px.line(data, x='timestamp', y='humidity', color='country',
                                       title='Real-Time Humidity by Country')
                fig_humidity.update_layout(xaxis_title='Time', yaxis_title='Humidity (%)', legend_title='Country')

                col1, col2 = st.columns(2)
                col1.plotly_chart(fig_temp, use_container_width=True)
                col2.plotly_chart(fig_humidity, use_container_width=True)

        elif response.status_code == 204:
            st.warning("No live data available at the moment.")
        else:
            st.error("Failed to fetch live data from API.")

    except Exception as e:
        st.error(f"Error fetching data: {e}")

    time.sleep(2)  # Her 2 saniyede bir veri güncelleniyor

# Altbilgi
st.markdown(
    """
    <footer>
        <div style="text-align: center;">Bu site <strong>Geliştirici Adı</strong> tarafından yapılmıştır.</div>
        <div style="text-align: center;">
            <a href="https://github.com/your-github" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30"></a>
            <a href="https://linkedin.com/in/your-linkedin" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30"></a>
        </div>
    </footer>
    """, unsafe_allow_html=True
)
