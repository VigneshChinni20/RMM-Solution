import random
import pandas as pd

# Create 100 clean rows of system metrics
data = []
for i in range(100):
    data.append({
        "CPU": random.randint(10, 100),
        "RAM": random.randint(10, 100),
        "Disk": random.randint(10, 100)
    })

# Build DataFrame with guaranteed correct columns
df = pd.DataFrame(data, columns=["CPU", "RAM", "Disk"])

# Save to CSV
df.to_csv("infrastructure_data.csv", index=False)
print("Clean data saved to infrastructure_data.csv")