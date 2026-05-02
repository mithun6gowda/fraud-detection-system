from kafka import KafkaConsumer
import json
import requests

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:
    txn = message.value

    response = requests.post(
        "http://localhost:8000/predict",
        json=txn
    )

    print("Txn:", txn)
    print("Prediction:", response.json())