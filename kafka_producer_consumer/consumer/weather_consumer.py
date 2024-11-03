from kafka import KafkaConsumer
import json

# Define Kafka Consumer
consumer = KafkaConsumer(
    'global_weather',  # topic name
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Start reading data from the beginning
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Decode data in JSON format
)

# Listening to data and displaying it in the terminal
for message in consumer:
    weather_data = message.value
    print(f"Received: {weather_data}")
"""Descriptions:
Consumer: You can read data from a certain topic with Kafka Consumer.
With the auto_offset_reset: oldest setting, Kafka Consumer can read all messages from the past.

value_deserializer: We get the JSON data from Kafka and show it in the screen by decoding it.

"""
