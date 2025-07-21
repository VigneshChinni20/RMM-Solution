import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load data
df = pd.read_csv("infrastructure_data.csv").dropna()

# Train model
model = IsolationForest(contamination=0.1)
model.fit(df)

# Save model
joblib.dump(model, "anomaly_model.pkl")

print("Model trained and saved as anomaly_model.pkl")