import pandas as pd
import time
from auto_fix import restart_service, log_event

# Keep monitoring for a fixed number of cycles
for i in range(10):
    df = pd.read_csv("infrastructure_data.csv").dropna()
    latest = df.iloc[-1]

    print(f"Check #{i+1}:")
    print(f"CPU: {latest['CPU']}%, RAM: {latest['RAM']}%, Disk: {latest['Disk']}%\n")

    if latest["CPU"] > 85:
        print("CPU overload!")
        restart_service()
        log_event("Loop fix: high CPU")

    if latest["RAM"] > 90:
        print("RAM spike!")
        restart_service()
        log_event("Loop fix: high RAM")

    if latest["Disk"] > 95:
        print("Low disk space!")
        restart_service()
        log_event("Loop fix: low disk")

    time.sleep(5)  # wait 5 seconds before checking again