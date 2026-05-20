import sys
import os
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)

df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)