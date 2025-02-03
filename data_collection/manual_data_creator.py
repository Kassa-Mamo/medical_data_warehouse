import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Create DataFrame & Save to CSV
df = pd.DataFrame(data)
df.to_csv("manual_data.csv", index=False)

print("CSV file created successfully!")
