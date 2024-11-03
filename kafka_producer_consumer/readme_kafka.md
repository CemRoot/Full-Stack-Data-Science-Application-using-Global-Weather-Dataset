# Kafka Weather Data Producer & Consumer Application

## Introduction

This project demonstrates how to utilize **Apache Kafka** for streaming weather data in real time. We implement a **Kafka Producer** to send weather information (such as location, temperature, humidity, etc.) from a CSV file into a Kafka topic and a **Kafka Consumer** to receive and display this data from the topic. Apache Kafka is a widely-used, distributed streaming platform suitable for real-time data pipelines and event-driven systems.

### Table of Contents

- [Kafka Producer](#kafka-producer)
- [Kafka Consumer](#kafka-consumer)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Why Use Kafka?](#why-use-kafka)
- [How to Run](#how-to-run)
- [Explanation of Functions](#explanation-of-functions)

---

## Kafka Producer

### Purpose

The Kafka Producer reads weather data from a CSV file and sends this data as individual messages to a Kafka topic named `global_weather`.

### Key Functions and Components:

- **`KafkaProducer`**: The core Kafka object used to send messages to a Kafka topic, containing weather details such as location, temperature, and humidity.
- **`value_serializer`**: Serializes the weather data to JSON format before sending it to Kafka, ensuring the data is structured and easily readable for the Consumer.
- **`producer.send()`**: Sends each row of weather data from the CSV file as a separate message to the `global_weather` topic.
- **`time.sleep(1)`**: Adds a 1-second delay between each message to simulate real-time data streaming.

---

## Kafka Consumer

### Purpose

The Kafka Consumer listens to the `global_weather` topic and receives messages containing weather data, displaying it in the terminal as it arrives.

### Key Functions and Components:

- **`KafkaConsumer`**: The main Kafka object used to retrieve messages from a Kafka topic. It continuously listens for new messages on the `global_weather` topic.
- **`value_deserializer`**: Decodes the JSON-encoded weather data back into a Python dictionary for easy access.
- **`auto_offset_reset='earliest'`**: Ensures the Consumer reads all messages from the beginning of the topic, including any past messages.
- **`for message in consumer:`**: A loop that continuously listens for new messages from the topic and displays them when received.

---

## Requirements

- **Python 3.6+**
- **Apache Kafka** (with Zookeeper)
- **pandas** (for reading the CSV file)
- **kafka-python** (Python client for Apache Kafka)
- **CSV file**: Weather data file, for instance `GlobalWeatherRepository.csv`

### Required Python Libraries:

```bash
pip install kafka-python pandas
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

5. **Run the Kafka Consumer**:
   Start listening for weather data messages on the `global_weather` topic.
   ```bash
   python weather_consumer.py
   ```

---

## Why Use Kafka?

Apache Kafka is ideal for applications requiring real-time data streaming. Kafka can efficiently manage high data volumes, provides fault tolerance, and scales well with demand. Common scenarios where Kafka is especially useful include:

- **Real-time data pipelines**: Kafka handles data streams reliably, making it perfect for streaming applications.
- **Event-driven systems**: In event-based architectures, Kafka is commonly used to process and respond to real-time data changes.

In this project, Kafka enables us to:

- Continuously stream weather data from a CSV file (Producer).
- Easily consume this data in real-time (Consumer).
- Scale both the Producer and Consumer as the data grows.

---

## How to Run

1. Ensure **Zookeeper** and **Kafka Server** are running.
2. Start the **Producer** script to send weather data:
   ```bash
   python weather_producer.py
   ```
3. Start the **Consumer** script to read weather data:
   ```bash
   python weather_consumer.py
   ```

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

### Kafka Consumer (weather_consumer.py)

- **`KafkaConsumer(topic, bootstrap_servers, auto_offset_reset, value_deserializer)`**:
    - Connects to Kafka and begins reading from the `global_weather` topic.
    - `auto_offset_reset='earliest'` ensures the Consumer reads messages from the beginning, capturing any older messages.

- **`for message in consumer:`**:
    - A loop that listens for incoming messages from Kafka, each containing weather data sent by the Producer.
---

## Conclusion

This project demonstrates a simple use case of Kafka as a distributed messaging system for weather data. Kafka allows us
to handle real-time data streams efficiently, making it a powerful tool for any system that requires high throughput and
scalability.

```

### Açıklamalar:
- Bu `README.md` dosyasında hem **Kafka Producer** hem de **Kafka Consumer** işlevleri açıklandı.
- Kullanılan her fonksiyonun ne işe yaradığı ve neden tercih edildiği detaylı bir şekilde açıklandı.
- Ayrıca Kafka'nın neden bu proje için uygun bir araç olduğu vurgulandı.

Bu şablonu projene ekleyebilirsin! Eğer başka bir bölüm ya da açıklama eklemek istersen, söylemekten çekinme.