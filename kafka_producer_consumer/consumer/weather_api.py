from flask import Flask, jsonify
import pandas as pd
from confluent_kafka import Consumer, KafkaError
import json

app = Flask(__name__)

# Cleaned weather data endpoint
@app.route('/data', methods=['GET'])
def get_cleaned_data():
    try:
        # Read CSV file
        data = pd.read_csv('/root/GlobalWeatherRepository.csv')
        return jsonify(data.to_dict(orient="records"))  # transform data to JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # return error message and 500 status code

# Live weather data endpoint
@app.route('/live', methods=['GET'])
def get_live_data():
    # Kafka Consumer Configuration
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',  # Kafka broker address
        'group.id': 'weather_group',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    consumer.subscribe(['global_weather'])

    live_data = []
    while True:
        msg = consumer.poll(1.0)  # 1 second timeout
        if msg is None:
            break
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                break
            else:
                print(f"Kafka error: {msg.error()}")
                break
        try:
            data = json.loads(msg.value().decode('utf-8'))
            live_data.append(data)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
        if len(live_data) >= 5:  # 5 data is enough
            break

    consumer.close()
    return jsonify(live_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
