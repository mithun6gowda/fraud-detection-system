import numpy as np

def create_features(txn,user_history):
    return{
        "amount":txn["amount"],
        "txn_velocity_1min":len(user_history[-10:]),
        "avg_amount":np.mean([t["amount"] for t in user_history]) if user_history else 0,
        "is_foreign":int(txn["location"]!="IN")
    }