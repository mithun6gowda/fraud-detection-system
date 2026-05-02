from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("models/fraud_model.pkl")

def transform(txn):
    is_foreign = int(txn["location"] != "IN")
    avg_amount = 200
    deviation = txn["amount"] - avg_amount

    return [txn["amount"], is_foreign, deviation]

@app.post("/predict")
def predict(txn: dict):
    try:
        features = transform(txn)

        score = model.predict_proba([features])[0][1]

        decision = "ALLOW"
        if score > 0.8:
            decision = "BLOCK"
        elif score > 0.5:
            decision = "REVIEW"

        return {
            "fraud_score": float(score),
            "decision": decision
        }

    except Exception as e:
        return {
            "error": str(e)
        }