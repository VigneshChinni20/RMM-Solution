import pandas as pd
import time
import joblib
from auto_fix import restart_service, log_event

model = joblib.load("anomaly_model.pkl")
print("Smart Monitor is syncing with data stream...\n")

last_index = -1  # Tracks the last row we processed

while True:
    df = pd.read_csv("infrastructure_data.csv").dropna()

    if len(df) > last_index + 1:
        latest = df.iloc[[-1]]
        last_index = len(df) - 1

        cpu = latest["CPU"].values[0]
        ram = latest["RAM"].values[0]
        disk = latest["Disk"].values[0]

        print(f"New Data: CPU {cpu}%, RAM {ram}%, Disk {disk}%")

        # Threshold checks
        if cpu > 85:
            print("CPU high! Restarting...")
            restart_service()
            log_event("Threshold fix: CPU overload")

        if ram > 90:
            print("RAM critical! Restarting...")
            restart_service()
            log_event("Threshold fix: RAM spike")

        if disk > 95:
            print("Disk nearly full! Restarting...")
            restart_service()
            log_event("Threshold fix: Disk warning")

        # ML prediction
        prediction = model.predict(latest)[0]
        score = model.decision_function(latest)[0]
        print(f"Prediction: {prediction} | Score: {score:.4f}")

        if prediction == -1:
            print("Anomaly detected! Auto-fix applied.")
            restart_service()
            log_event(f"ML fix: Anomaly | Score {score:.4f}")

        # Log prediction to anomaly_log.csv
        with open("anomaly_log.csv", "a") as log:
            log.write(f"{cpu},{ram},{disk},{prediction},{score:.4f}\n")

        print("-" * 50)

    time.sleep(2)  # Wait before checking again