import pandas as pd
import joblib
from auto_fix import restart_service, log_event

df = pd.read_csv("infrastructure_data.csv").dropna()
latest = df.iloc[[-1]]  # double brackets to keep DataFrame shape

model = joblib.load("anomaly_model.pkl")
prediction = model.predict(latest)[0]

print(f"Prediction result: {prediction}")

if prediction == -1:
    print("Anomaly detected!")
    restart_service()
    log_event("ML fix: anomaly detected")
else:
    print("System looks normal.")