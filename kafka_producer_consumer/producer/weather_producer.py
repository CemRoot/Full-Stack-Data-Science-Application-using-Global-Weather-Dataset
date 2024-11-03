from kafka import KafkaProducer
import pandas as pd
import time
import json
import os

# Veri dosyasını göreceli bir yoldan yüklüyoruz
data = pd.read_csv(
    r'C:\Users\eminc\OneDrive\Desktop\NATIONAL-COLLEGE-OF-IRELAND-LESSONS-LABS\LABS\Programming for Artificial Intelligence (MSCAI1) LAB\CA_Cem-Koyluoglu\app\GlobalWeatherRepository.csv')

# Kafka producer tanımlaması
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Her satırı Kafka'ya gönderiyoruz
for index, row in data.iterrows():
    weather_data = {
        "location": row["location_name"],
        "country": row["country"],
        "temperature": row["temperature_celsius"],
        "condition": row["condition_text"],
        "last_updated": row["last_updated"]
    }
    producer.send('global_weather', value=weather_data)
    print(f"Sent data: {weather_data}")
    time.sleep(1)

producer.flush()
producer.close()
print("Producer finished")
