from flask import Flask, jsonify
import pandas as pd
from confluent_kafka import Consumer, KafkaError
import json

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_cleaned_data():
    try:
        data = pd.read_csv('/root/GlobalWeatherRepository.csv')
        return jsonify(data.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/live', methods=['GET'])
def get_live_data():
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'new_weather_group',  # Yeni bir group id kullandık
        'auto.offset.reset': 'earliest'    # En baştan başlamak için ayar
    }
    try:
        consumer = Consumer(consumer_conf)
        consumer.subscribe(['global_weather'])

        live_data = []
        msgs = consumer.consume(num_messages=5, timeout=0.5)  # 5 mesajı bir defada çekme
        for msg in msgs:
            if msg is None:
                continue
            if msg.error():
                print(f"Kafka error: {msg.error()}")
                continue
            try:
                data = json.loads(msg.value().decode('utf-8'))
                live_data.append(data)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
        consumer.close()
        if not live_data:
            return jsonify({"error": "No live data received from Kafka."}), 204
        return jsonify(live_data)
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
