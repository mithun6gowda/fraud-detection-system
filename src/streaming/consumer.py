from confluent_kafka import Consumer
import json
import requests

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'fraud-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['transactions'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Error:", msg.error())
        continue

    txn = json.loads(msg.value().decode('utf-8'))

    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json=txn
        )
        print("Txn:", txn)
        print("Prediction:", response.json())
    except Exception as e:
        print("API Error:", e)