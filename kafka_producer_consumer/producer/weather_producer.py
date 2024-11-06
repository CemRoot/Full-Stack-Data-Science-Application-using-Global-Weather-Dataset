from kafka import KafkaProducer
import pandas as pd
import time
import json

data = pd.read_csv('/root/GlobalWeatherRepository.csv')

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for index, row in data.iterrows():
    weather_data = {
        "location": row["location_name"],
        "country": row["country"],
        "temperature": row["temperature_celsius"],
        "humidity": row["humidity"],
        "latitude": row["latitude"],
        "longitude": row["longitude"],
        "condition": row["condition_text"],
        "last_updated": row["last_updated"]
    }
    producer.send('global_weather', value=weather_data)
    print(f"Sent data: {weather_data}")
    time.sleep(0.2)  # Gönderim süresini düşürdük

producer.flush()
producer.close()
print("Producer finished")
