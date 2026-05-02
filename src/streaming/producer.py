from kafka import KafkaProducer

import json ,time, random 


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    return {

        "user_id":round.randint(1,1000),
        "amount":round(random.uniform(10,5000),2),
        "location": random.choice(["IN", "US", "UK"]),
        "device": random.choice(["mobile", "web"]),
        "timestamp": time.time()
        }

while True:
    txn = generate_transaction()
    producer.send("transactions", txn)
    print("Sent:", txn)
    time.sleep(0.1)