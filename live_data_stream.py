import pandas as pd
import random
import time

while True:
    new_row = {
        "CPU": random.randint(10, 100),
        "RAM": random.randint(10, 100),
        "Disk": random.randint(10, 100)
    }

    df = pd.DataFrame([new_row])
    df.to_csv("infrastructure_data.csv", mode="a", header=False, index=False)

    print(f"Added: CPU {new_row['CPU']}%, RAM {new_row['RAM']}%, Disk {new_row['Disk']}%")
    time.sleep(5)