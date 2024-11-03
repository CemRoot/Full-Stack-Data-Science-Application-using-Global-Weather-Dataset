from kafka import KafkaProducer
import pandas as pd
import time
import json

# DigitalOcean Server send data to Kafka
data = pd.read_csv('/root/GlobalWeatherRepository.csv')

# Kafka producer create
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Each row of the data is sent to the Kafka topic
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
    time.sleep(1)  # 1second delay between data sending

# Close the producer
producer.flush()
producer.close()
print("Producer finished")
