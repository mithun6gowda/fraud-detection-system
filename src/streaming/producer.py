from confluent_kafka import Producer
import json, time, random

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def generate_transaction():
    return {
        "user_id": random.randint(1, 1000),
        "amount": round(random.uniform(10, 5000), 2),
        "location": random.choice(["IN", "US", "UK"]),
        "device": random.choice(["mobile", "web"])
    }

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")

while True:
    txn = generate_transaction()
    producer.produce(
        "transactions",
        value=json.dumps(txn),
        callback=delivery_report
    )
    producer.flush()
    print("Sent:", txn)
    time.sleep(1)