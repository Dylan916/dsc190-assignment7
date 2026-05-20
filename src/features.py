import sys
import os
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)

df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = pd.to_datetime(df["date"]).dt.strftime("%A")

os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)