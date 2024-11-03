***

# Global Dashboard for Weather Data

**Languages**: English | Türkçe

---

## English

### Project Review

Made using Python, Flask, Kafka, and Streamlit, the **Global Weather Data Dashboard** is a real-time data visualization tool. Through a web interface, users of this dashboard may access real-time and historical worldwide weather data. The project replicating meteorological data updates over Kafka and dynamically displaying them dynamically in a Streamlit web application seeks to show data streaming and real-time visualization capabilities.
### Essential Technologies

- **Flask** : Designed to provide a REST API running live updates over Kafka over cleansed weather data.
- **Kafka** : Simulates realtime updates by streaming real-time weather data.
- Designed for showing data visualizations and dashboard interface creation, **Streamlit** is a Python framework.
- Applied for interactive and dynamic data visualization within the Streamlit application: **Plotly**

### File Organization and Reasoning

1. **app.py**
   - This file arranges the **Flask** REST API for the project.
   - Purposes:
     -   Indicates the API is operating with a basic message on the homepage **home()**.
     - **`get_cleaned_data()`**: Reads the cleaned weather data from a CSV file and returns it in JSON format via the `/data` endpoint. This allows the Streamlit app to load historical weather data.
     - **`get_live_data()`**: Consumes live weather data from Kafka's `global_weather` topic and returns it in JSON format via the `/live` endpoint.

2. **weather_producer.py**
   - This script generates real-time weather data updates by sending each data row from the CSV file to the Kafka `global_weather` topic.
   - Functions:
     - **`KafkaProducer()`**: Sets up a producer to send messages (weather data) to the Kafka topic.
     - **`producer.send()`**: Sends a new weather data message to Kafka every second, simulating real-time updates.

3. **weather_dashboard.py**
   - This is the main **Streamlit** application file.
   - Functions:
     - **`load_data()`**: Uses `requests.get` to fetch cleaned data from the Flask API. Cached to improve loading speed and reduce API calls.
     - **`get_live_data()`**: Fetches live weather data from the Flask API’s `/live` endpoint and displays it dynamically in a Streamlit table and chart.
     - **`st.selectbox()`**: Allows users to set the refresh rate for live data updates, improving interactivity and user control.
     - **`px.line()`**: From Plotly, used to create a dynamic line chart that updates based on live data.

### How to Run

1. Start **Kafka and Zookeeper**:
   ```bash
   zookeeper-server-start.sh config/zookeeper.properties
   kafka-server-start.sh config/server.properties
   ```

2. Run the **Flask API**:
   ```bash
   python app.py
   ```

3. Start the **Kafka Producer**:
   ```bash
   python weather_producer.py
   ```

4. Run the **Streamlit App**:
   ```bash
   streamlit run weather_dashboard.py
   ```

### Customization

The Streamlit app allows you to choose a refresh rate via the top right corner's `selectbox`. For data stream updating, choose 1, 2, 5, or 10 secondslllllllllllllll
### Libraries and Modules

| Library/Module  | Purpose |
|-----------------|---------|
| `Flask`         | Provides API endpoints for serving cleaned and live weather data |
| `pandas`        | Reads and processes CSV data for the API |
| `kafka-python`  | Sends and receives data in real-time from Kafka topics |
| `Streamlit`     | Builds the web interface and displays dynamic visualizations |
| `Plotly`        | Creates interactive charts in the Streamlit app |

---

## Türkçe

### Proje Genel Bakış

**Global Hava Durumu Verisi Panosu**, Python, Flask, Kafka ve Streamlit kullanılarak geliştirilen gerçek zamanlı bir veri görselleştirme aracıdır. Bu pano, kullanıcıların web arayüzü üzerinden tarihsel ve gerçek zamanlı global hava durumu verilerini görüntülemesini sağlar. Projenin amacı, Kafka üzerinden hava durumu verisi güncellemelerini simüle ederek veri akışı ve gerçek zamanlı görselleştirme yeteneklerini sergilemektir.

### Ana Teknolojiler

- **Flask**: Temizlenmiş hava durumu verisini sunan ve Kafka üzerinden canlı güncellemeler sağlayan bir REST API oluşturmak için kullanıldı.
- **Kafka**: Gerçek zamanlı hava durumu veri akışı sağlamak için kullanıldı.
- **Streamlit**: Pano arayüzünü oluşturmak ve veri görselleştirmelerini göstermek için kullanıldı.
- **Plotly**: Streamlit uygulaması içinde etkileşimli ve dinamik veri görselleştirmeleri için kullanıldı.

### Dosya Yapısı ve Açıklama

1. **app.py**
   - Bu dosya, proje için **Flask** REST API’sini kurar.
   - Fonksiyonlar:
     - **`home()`**: API’nin çalıştığını belirten basit bir mesaj gösterir.
     - **`get_cleaned_data()`**: Temizlenmiş hava durumu verisini CSV dosyasından okur ve `/data` endpoint'i üzerinden JSON formatında döner. Bu fonksiyon, Streamlit uygulamasının tarihsel veriyi yüklemesini sağlar.
     - **`get_live_data()`**: Kafka’daki `global_weather` topic’inden canlı hava durumu verisini tüketir ve `/live` endpoint'i üzerinden JSON formatında döner.

2. **weather_producer.py**
   - Bu betik, her bir CSV satırını Kafka `global_weather` topic’ine göndererek gerçek zamanlı hava durumu güncellemelerini simüle eder.
   - Fonksiyonlar:
     - **`KafkaProducer()`**: Kafka topic’ine mesaj (hava durumu verisi) göndermek için bir producer oluşturur.
     - **`producer.send()`**: Her saniyede bir yeni hava durumu mesajını Kafka’ya göndererek gerçek zamanlı güncellemeler simüle eder.

3. **weather_dashboard.py**
   - Bu, ana **Streamlit** uygulama dosyasıdır.
   - Fonksiyonlar:
     - **`load_data()`**: Temizlenmiş veriyi Flask API’den almak için `requests.get` kullanır. Yükleme hızını artırmak için önbelleğe alınmıştır.
     - **`get_live_data()`**: Flask API’nin `/live` endpoint'inden canlı veriyi alır ve bu veriyi Streamlit tablosunda ve grafiğinde dinamik olarak gösterir.
     - **`st.selectbox()`**: Kullanıcıların canlı veri güncelleme hızını seçmesine olanak tanır.
     - **`px.line()`**: Plotly’den gelen ve canlı veriye bağlı olarak güncellenen dinamik bir çizgi grafik oluşturur.

### Çalıştırma Adımları

1. **Kafka ve Zookeeper’ı Başlatın**:
   ```bash
   zookeeper-server-start.sh config/zookeeper.properties
   kafka-server-start.sh config/server.properties
   ```

2. **Flask API’yi Çalıştırın**:
   ```bash
   python app.py
   ```

3. **Kafka Producer’ı Başlatın**:
   ```bash
   python weather_producer.py
   ```

4. **Streamlit Uygulamasını Çalıştırın**:
   ```bash
   streamlit run weather_dashboard.py
   ```

### Özelleştirme

Streamlit uygulamasında, sağ üst köşedeki `selectbox` kullanarak yenileme hızını seçebilirsiniz. Veri akışını güncellemek için 1, 2, 5 veya 10 saniye arasından bir seçim yapabilirsiniz.

### Kütüphane ve Modüller

| Kütüphane/Modül  | Amaç |
|------------------|------|
| `Flask`          | Temizlenmiş ve canlı hava durumu verisini sunmak için API endpoint'leri sağlar |
| `pandas`         | API için CSV verisini okur ve işler |
| `kafka-python`   | Gerçek zamanlı veri akışını Kafka topic'lerinden alır ve gönderir |
| `Streamlit`      | Web arayüzünü kurar ve dinamik görselleştirmeler gösterir |
| `Plotly`         | Streamlit uygulamasında etkileşimli grafikler oluşturur |

---