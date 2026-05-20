import sys
import os
import pandas as pd

VALID_EVENT_TYPES = {"click", "login", "scroll", "view", "purchase"}

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)

df = df.dropna(subset=["user_id", "timestamp", "event_type", "duration_seconds"])

df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

df = df[df["duration_seconds"] > 0]

df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed").dt.strftime("%Y-%m-%dT%H:%M:%S")

os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)