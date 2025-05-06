# Importing Packages
import json
import pandas as pd

# Path to honeypot logs
LOG_FILE = "logs/honeypot_logs.jsonl"

# Output Data File
OUTPUT_CSV = "dataset.csv"

# Storage of Parsed Records
data = []

# Reading logs line by line
with open(LOG_FILE, "r") as f:
    for line in f:
        try:
            entry = json.loads(line.strip())

            method = entry.get("method", "GET")
            path = entry.get("path", "")
            headers = entry.get("headers", {})
            body = entry.get("body", "")
            user_agent = entry.get("user_agent", "")

            # Collecting Data
            record = {
                "method_GET": 1 if method.upper() == "GET" else 0,
                "method_POST": 1 if method.upper() == "POST" else 0,
                "path_length": len(path),
                "header_count": len(headers),
                "body_length": len(body),
                "has_user_agent": 1 if user_agent else 0,

                # O if benign, 1 if malicious
            }

            data.append(record)

        except json.JSONDecodeError:
            print("Skipped Bad Line")

# Creating DataFrame
df = pd.DataFrame(data)

# Saving to CSV variable
df.to_csv(OUTPUT_CSV, index=False)

# See num of entries
print(f"Parsed {len(df)} entries, saved to CSV.")