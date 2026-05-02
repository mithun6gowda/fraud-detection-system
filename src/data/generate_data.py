import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

NUM_USERS = 1000
NUM_TRANSACTIONS = 100000

data = []

user_profiles = {}

# Create user profiles
for user_id in range(NUM_USERS):
    user_profiles[user_id] = {
        "home_country": random.choice(["IN", "US", "UK"]),
        "avg_amount": random.uniform(50, 500)
    }

def generate_transaction(user_id):
    profile = user_profiles[user_id]

    # Normal behavior
    amount = np.random.normal(profile["avg_amount"], 50)
    location = profile["home_country"]

    is_fraud = 0

    # Fraud patterns
    if random.random() < 0.05:  # 5% fraud
        is_fraud = 1

        fraud_type = random.choice(["high_amount", "foreign", "velocity"])

        if fraud_type == "high_amount":
            amount *= 10

        elif fraud_type == "foreign":
            location = random.choice(["CN", "RU", "BR"])

        elif fraud_type == "velocity":
            amount *= 2

    return {
        "user_id": user_id,
        "amount": abs(amount),
        "location": location,
        "is_fraud": is_fraud
    }

# Generate data
for _ in range(NUM_TRANSACTIONS):
    user_id = random.randint(0, NUM_USERS - 1)
    txn = generate_transaction(user_id)
    data.append(txn)

df = pd.DataFrame(data)
df.to_csv("src/data/fraud_data.csv", index=False)

print("Dataset generated:", df.shape)