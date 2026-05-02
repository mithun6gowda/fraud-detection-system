import pandas as pd
import numpy as np
from xgboost import XGBClassifier

import joblib

df = pd.read_csv("data/fraud_data.csv")

df["is_foreign"] = (df["location"]!="IN").astype(int)


user_avg = df.groupby("user_id")["amount"].transform("mean")
df["deviation_from_avg"] = df["amount"] - user_avg

features = ["amount", "is_foreign", "deviation_from_avg"]
X = df[features]
y = df["is_fraud"]

model = XGBClassifier(scale_pos_weight=20,n_estimators=100,max_depth=5)

model.fit(X,y)

joblib.dump(model,"models/fraud_model.pkl")

print("model trained and saved")