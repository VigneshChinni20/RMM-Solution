from flask import Flask
import pandas as pd
import joblib

app = Flask(__name__)

# Load the ML model once
model = joblib.load("anomaly_model.pkl")

@app.route("/")
def home():
    try:
        # Load data and get the latest row
        df = pd.read_csv("infrastructure_data.csv").dropna()
        latest = df.iloc[[-1]]  # Double brackets keep it as DataFrame
        row = df.iloc[-1]       # Single row for numbers

        cpu = row["CPU"]
        ram = row["RAM"]
        disk = row["Disk"]

        # Run prediction and score
        prediction = model.predict(latest)[0]
        score = model.decision_function(latest)[0]

        # Translate prediction to label
        status = "NORMAL" if prediction == 1 else "ANOMALY"

        # Build the HTML response
        return f"""
            <h1>AI RMM Dashboard</h1>
            <p>CPU Usage: {cpu}%</p>
            <p>RAM Usage: {ram}%</p>
            <p>Disk Usage: {disk}%</p>
            <p>Prediction: {status}</p>
            <p>Anomaly Score: {score:.4f}</p>
        """
    except:
        return "<h1>AI RMM Dashboard</h1><p>No data or prediction available.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)