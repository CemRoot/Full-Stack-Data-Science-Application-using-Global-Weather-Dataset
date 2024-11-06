# Kafka Weather Data Producer & Consumer Application

## Language Options:
- [English](#Introduction)
- [Türkçe](#giriş)

---
# Kafka Hava Durumu Verisi Üretici & Tüketici Uygulaması

## Giriş

Bu proje, **Apache Kafka** kullanarak gerçek zamanlı hava durumu verilerini akış halinde işlemek için geliştirilmiştir. Proje, bir **Kafka Üreticisi** (Producer) ile CSV dosyasından hava durumu verilerini bir Kafka konusuna (topic) gönderir ve bu verileri bir **Kafka Tüketicisi** (Consumer) üzerinden bir Flask API aracılığıyla sunar. Bu uygulama, **DigitalOcean Ubuntu sunucusu** üzerinde çalışmaktadır. Apache Kafka, gerçek zamanlı veri boru hatları ve olay tabanlı sistemler için yaygın olarak kullanılan bir dağıtık akış platformudur.

### İçindekiler

- [Weather_api.py](#weather_apipy)
- [Weather_producer.py](#weather_producerpy)
- [Gereksinimler](#gereksinimler)
- [Kurulum Talimatları](#kurulum-talimati)
- [Sunucu Yönetim Komutları](#sunucu-yonetim-komutlari)
- [Neden Kafka Kullanmalıyız?](#neden-kafka-kullanmaliyiz)
- [Çalıştırma Yöntemi](#calistirma-yontemi)
- [Fonksiyonların Açıklaması](#fonksiyonlarin-aciklamasi)
- [Sonuç](#son

uc)

---

## Weather_api.py

Bu Flask script'i, **DigitalOcean Ubuntu sunucusu** üzerinde hava durumu verilerini REST API aracılığıyla sunar.

İki ana uç noktaya sahiptir:

- **"/data"**: Bu uç nokta, "/root/" konumundaki "GlobalWeatherRepository.csv" dosyasından hava durumu verilerini okur ve JSON formatında döndürür.
- **"/live"**: Bu uç nokta, "global_weather" konusundan canlı hava durumu verilerini alır. Kafka tüketicisi, yerel bir Kafka broker'a bağlanır ve beş kayıta kadar veri okur veya hiç veri bulunamadığında işlemi sonlandırır.

Pandas kullanarak CSV dosyasından okunan veriler, API üzerinden JSON formatında kolayca erişilebilir.

Script, JSON çözümleme ve Kafka hatalarını yöneterek daha sağlam bir hata yönetimi sağlar.

Program, **0.0.0.0** üzerinde **5000 portu** ile debug modda çalışır.

---

## Weather_producer.py

Bu script, **DigitalOcean sunucusundaki** **"/root/GlobalWeatherRepository.csv"** konumundan hava durumu verilerini okur ve bunları Kafka'ya gönderir.

Bu veriler, **"global_weather"** konusuna bir Kafka Üreticisi kullanılarak gönderilir.

Script, her CSV satırından konum, ülke, sıcaklık, durum ve güncellenme zamanı bilgilerini alır ve JSON formatına dönüştürür.

Mesajlar arasında bir saniyelik duraklamalarla JSON verileri **localhost:9092** adresindeki Kafka broker'a gönderilir.

Veri üretim süreci tamamlandığında, üretici bağlantısı temizlenir ve kapatılır.

---

## Gereksinimler

- **Python 3.6+**
- **Apache Kafka** (Zookeeper ile)
- **pandas** (CSV dosyasını okumak için)
- **confluent_kafka** (Flask API'deki Kafka Tüketicisi için)
- **flask** (API oluşturmak için)
- **kafka-python** (Kafka Üreticisi için)
- **CSV dosyası**: Hava durumu verileri dosyası, örneğin `GlobalWeatherRepository.csv`

### Gerekli Python Kütüphaneleri:

```bash
pip install kafka-python pandas confluent_kafka flask
```

---

## Kurulum Talimatları

1. **Zookeeper'ı Başlatın**:
   Kafka'yı başlatmadan önce Zookeeper'ın çalıştığından emin olun, çünkü Kafka Zookeeper'a bağlıdır.
   ```bash
   .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
   ```

2. **Kafka Sunucusunu Başlatın**:
   Kafka broker'ı başlatın.
   ```bash
   .\bin\windows\kafka-server-start.bat .\config\server.properties
   ```

3. **Kafka Konusu Oluşturun**:
   Otomatik konu oluşturma devre dışıysa, isteğe bağlı olarak `global_weather` adlı bir Kafka konusu oluşturun.
   ```bash
   .\bin\windows\kafka-topics.bat --create --topic global_weather --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

4. **Kafka Üreticisini Çalıştırın**:
   CSV dosyasından `global_weather` konusuna hava durumu verilerini gönderin.
   ```bash
   python weather_producer.py
   ```

5. **Flask Kafka Tüketici API'sini Çalıştırın**:
   Statik ve canlı hava durumu verilerine erişim sağlayan Flask API'sini başlatın.
   ```bash
   python weather_api.py
   ```

---

## Sunucu Yönetim Komutları

### Servisleri Durdurma

DigitalOcean üzerindeki sunucu kaynaklarını verimli yönetmek için gereksiz servisleri aşağıdaki komutlarla durdurabilirsiniz:

- **Flask API'yi Durdurun**:
  ```bash
  sudo systemctl stop weather_api.service
  ```
- **Üreticiyi Durdurun**:
  ```bash
  sudo systemctl stop weather_producer.service
  ```
- **Kafka'yı Durdurun**:
  ```bash
  pkill -f kafka.Kafka
  ```
- **Zookeeper'ı Durdurun**:
  ```bash
  pkill -f zookeeper
  ```

### Servisleri Yeniden Başlatma veya Başlatma

Her servisi yeniden başlatmak veya başlatmak için aşağıdaki komutları kullanın:

- **Zookeeper'ı Başlatın**:
  ```bash
  /usr/local/kafka/bin/zookeeper-server-start.sh -daemon /usr/local/kafka/config/zookeeper.properties
  ```
- **Kafka'yı Başlatın**:
  ```bash
  /usr/local/kafka/bin/kafka-server-start.sh -daemon /usr/local/kafka/config/server.properties
  ```
- **Flask API'yi Başlatın**:
  ```bash
  sudo systemctl start weather_api.service
  ```
- **Üreticiyi Başlatın**:
  ```bash
  sudo systemctl start weather_producer.service
  ```

### Servis Durumunu Kontrol Etme

Servislerin çalışıp çalışmadığını kontrol etmek için:

- **Flask API'nin durumunu kontrol edin**:
  ```bash
  sudo systemctl status weather_api.service
  ```
- **Üreticinin durumunu kontrol edin**:
  ```bash
  sudo systemctl status weather_producer.service
  ```

---

## Neden Kafka Kullanmalıyız?

Apache Kafka, gerçek zamanlı veri akışı gerektiren uygulamalar için idealdir. Kafka, yüksek veri hacimlerini verimli bir şekilde yönetir, hata toleransı sağlar ve talebe göre ölçeklenebilir. Kafka'nın özellikle faydalı olduğu bazı durumlar şunlardır:

- **Gerçek zamanlı veri boru hatları**: Kafka, veri akışlarını güvenilir bir şekilde yönetir ve bu da onu akış uygulamaları için mükemmel bir hale getirir.
- **Olay tabanlı sistemler**: Olay bazlı mimarilerde Kafka, gerçek zamanlı veri değişikliklerini işlemek ve yanıt vermek için yaygın olarak kullanılır.

Bu projede, Kafka sayesinde:

- CSV dosyasından sürekli olarak hava durumu verisi akışı sağlanır (Üretici).
- Bu veriler gerçek zamanlı olarak kolayca tüketilir (Tüketici).
- Veri büyüdükçe Üretici ve Tüketici'nin ölçeklendirilmesi kolaylaşır.

---

## Çalıştırma Yöntemi

1. **Zookeeper** ve **Kafka Sunucusu**nun çalıştığından emin olun.
2. Hava durumu verisini göndermek için **Üretici** script'ini başlatın:
   ```bash
   python weather_producer.py
   ```
3. Hava durumu verisini almak için **Flask Kafka Tüketici API'sini** başlatın:
   ```bash
   python weather_api.py
   ```

API uç noktalarına erişim:

- **Statik veri**: [http://localhost:5000/data](http://localhost:5000/data)
- **Canlı veri**: [http://localhost:5000/live](http://localhost:5000/live)

---

## Fonksiyonların Açıklaması

### Kafka Üretici (weather_producer.py)

- **`KafkaProducer(bootstrap_servers, value_serializer)`**:
    - `localhost:9092` adresinde çalışan Kafka broker'a bağlanır.
    - `value_serializer`, veriyi JSON formatında serileştirir ve Kafka'ya göndermeden önce yapılandırır.

- **`producer.send('global_weather', value=weather_data)`**:
    - Her bir hava durumu verisini `global_weather` konusuna gönderir.

- **`producer.flush()`**:
    - Üretici kapanmadan önce tüm birikmiş mesajların Kafka'ya gönderildiğinden emin olur.

### Flask Kafka Tüketici API'si (weather_api.py)

- **`/data` Uç Noktası**:
    - `GlobalWeatherRepository.csv` dosyasından hava durumu verilerini okur ve Pandas kullanarak JSON formatında döndürür.

- **`/live` Uç Noktası**:
    - Kafka'ya bağlanır ve `global_weather` konusundan beş kayıta kadar veri okur. Veri JSON formatında sunulur, böylece müşteriler canlı hava durumu güncellemelerini alabilir.

---

## Sonuç

Bu proje, **DigitalOcean Ubuntu sunucusu** üzerinde hava durumu verileri için Kafka'nın dağıtık bir mesajlaşma sistemi olarak basit bir kullanımını göstermektedir. Kafka, gerçek zamanlı veri akışlarını verimli bir şekilde yönetmemizi sağlar ve yüksek veri aktarım hızı ile ölçeklenebilirlik gerektiren sistemler için güçlü bir araçtır.

---

# Kafka Weather Data Producer & Consumer Application

## Introduction

This project demonstrates how to utilize **Apache Kafka** for streaming weather data in real time on a **DigitalOcean Ubuntu server**. The application includes a **Kafka Producer** that sends weather information (such as location, temperature, and condition) from a CSV file into a Kafka topic, and a **Kafka Consumer** served via a Flask API that retrieves and displays this data from the topic. Apache Kafka is a widely-used, distributed streaming platform suitable for real-time data pipelines and event-driven systems.

### Table of Contents

- [Weather_api.py](#weather_apipy)
- [Weather_producer.py](#weather_producerpy)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Server Management Commands](#server-management-commands)
- [Why Use Kafka?](#why-use-kafka)
- [How to Run](#how-to-run)
- [Explanation of Functions](#explanation-of-functions)
- [Conclusion](#conclusion)

---

## Weather_api.py

This Flask script serves weather data over a REST API on a DigitalOcean Ubuntu server.

It has two primary endpoints:

- **"/data"**: This endpoint receives weather data from "GlobalWeatherRepository.csv" located at "/root/" and returns it in JSON format.
- **"/live"**: This endpoint obtains live weather data from "global_weather." The Kafka consumer connects to a local broker and reads five records or until no more records are discovered.

Customers may easily consume the data, which is read via Pandas from the CSV, through the API in JSON format.

The script handles JSON decoding and Kafka faults for better error handling.

The program runs in debug mode on **0.0.0.0** and **port 5000**.

---

## Weather_producer.py

This script reads weather data from **"/root/GlobalWeatherRepository.csv"** on the DigitalOcean server.

This data is sent to **"global_weather"** in Kafka using a producer.

The script pulls location, nation, temperature, condition, and latest updated information from each CSV entry and converts them to JSON format.

There is a one-second pause between JSON messages sent to the Kafka broker on **localhost:9092**.

After flushing and closing the producer connection, data production is complete.

---

## Requirements

- **Python 3.6+**
- **Apache Kafka** (with Zookeeper)
- **pandas** (for reading the CSV file)
- **confluent_kafka** (for Kafka Consumer in Flask API)
- **flask** (for creating the API)
- **kafka-python** (for Kafka Producer)
- **CSV file**: Weather data file, such as `GlobalWeatherRepository.csv`

### Required Python Libraries:

```bash
pip install kafka-python pandas confluent_kafka flask
```

---

## Setup Instructions

1. **Start Zookeeper**:
   Make sure Zookeeper is running before starting Kafka, as Kafka relies on Zookeeper.
   ```bash
   .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
   ```

2. **Start Kafka Server**:
   Launch the Kafka broker.
   ```bash
   .\bin\windows\kafka-server-start.bat .\config\server.properties
   ```

3. **Set Up Kafka Topic**:
   Optionally, create a Kafka topic named `global_weather` if automatic topic creation is disabled.
   ```bash
   .\bin\windows\kafka-topics.bat --create --topic global_weather --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

4. **Run the Kafka Producer**:
   Send weather data from the CSV file to the `global_weather` topic.
   ```bash
   python weather_producer.py
   ```

5. **Run the Flask Kafka Consumer API**:
   Start the Flask API, which provides endpoints to access static and live weather data.
   ```bash
   python weather_api.py
   ```

---

## Server Management Commands

### Stopping Services

To manage server resources effectively on DigitalOcean, you can stop any unnecessary services using the following commands:

- **Stop Flask API**:
  ```bash
  sudo systemctl stop weather_api.service
  ```
- **Stop Producer**:
  ```bash
  sudo systemctl stop weather_producer.service
  ```
- **Stop Kafka**:
  ```bash
  pkill -f kafka.Kafka
  ```
- **Stop Zookeeper**:
  ```bash
  pkill -f zookeeper
  ```

### Restarting or Starting Services

Use the following commands to restart or start each service:

- **Start Zookeeper**:
  ```bash
  /usr/local/kafka/bin/zookeeper-server-start.sh -daemon /usr/local/kafka/config/zookeeper.properties
  ```
- **Start Kafka**:
  ```bash
  /usr/local/kafka/bin/kafka-server-start.sh -daemon /usr/local/kafka/config/server.properties
  ```
- **Start Flask API**:
  ```bash
  sudo systemctl start weather_api.service
  ```
- **Start Producer**:
  ```bash
  sudo systemctl start weather_producer.service
  ```

### Checking Service Status

To verify if services are running:

- **Check the status of Flask API**:
  ```bash
  sudo systemctl status weather_api.service
  ```
- **Check the status of Producer**:
  ```bash
  sudo systemctl status weather_producer.service
  ```

---

## Why Use Kafka?

Apache Kafka is ideal for applications requiring real-time data streaming. Kafka can efficiently manage high data volumes, provides fault tolerance, and scales well with demand. Common scenarios where Kafka is especially useful include:

- **Real-time data pipelines**: Kafka handles data streams reliably, making it perfect for streaming applications.
- **Event-driven systems**: In event-based architectures, Kafka is commonly used to process and respond to real-time data changes.

In this project, Kafka enables us to:

- Continuously stream weather data from a CSV file (Producer).
- Easily consume this data in real-time through a Flask API (Consumer).
- Scale both the Producer and Consumer as the data grows.

---

## How to Run

1. Ensure **Zookeeper** and **Kafka Server** are running.
2. Start the **Producer** script to send weather data:
   ```bash
   python weather_producer.py
   ```
3. Start the **Flask Kafka Consumer API** to read weather data:
   ```bash
   python weather_api.py
   ```

Access the API endpoints:

- **Static data**: [http://localhost:5000/data](http://localhost:5000/data)
- **Live data**: [http://localhost:5000/live](http://localhost:5000/live)

---

## Explanation of Functions

### Kafka Producer (weather_producer.py)

- **`KafkaProducer(bootstrap_servers, value_serializer)`**:
    - Connects to the Kafka broker running at `localhost:9092`.
    - `value_serializer` serializes the data as JSON before sending it to Kafka.

- **`producer.send('global_weather', value=weather_data)`**:
    - Sends each row of weather data to the `global_weather` topic on Kafka.

- **`producer.flush()`**:
    - Ensures that all buffered messages are sent to Kafka before closing the Producer.

### Flask Kafka Consumer API (weather_api.py)

- **`/data` Endpoint**:
    - Reads weather data from `GlobalWeatherRepository.csv` and returns it in JSON format using Pandas.

- **`/live` Endpoint**:
    - Connects to Kafka and reads up to five records from the `global_weather` topic. The data is served in JSON format, allowing clients to retrieve live weather updates.

---

## Conclusion

This project demonstrates a simple use case of Kafka as a distributed messaging system for weather data on a **DigitalOcean Ubuntu server**. Kafka allows us to handle real-time data streams efficiently, making it a powerful tool for any system that requires high throughput and scalability.

---




Go to up [English](#Introduction)
OR Go to up [Türkçe](#giriş)