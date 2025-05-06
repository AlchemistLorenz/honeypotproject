import pandas as pd

# Paths for CSVs
INPUT_CSV = "dataset.csv"
OUTPUT_CSV = "labeled_dataset.csv"

# Load dataset
df = pd.read_csv(INPUT_CSV)

# Add label column if missing
if 'label' not in df.columns:
    df['label'] = None

print("Auto-labeling honeypot dataset...")

# Benign traffic
benign_filter = (
    (df['label'].isna()) &
    (df['method_POST'] == 1) &
    (df['body_length'] > 10) &
    (df['path_length'] < 15) &
    (df['has_user_agent'] == 1)
)
df.loc[benign_filter, "label"] = 0
print(f"Auto-labeled {benign_filter.sum()} rows as benign (label=0)")

# Malicious traffic
malicious_filter = (
    (df['label'].isna()) &
    (df['method_GET'] == 1) &
    (df['body_length'] == 0) &
    (df['has_user_agent'] == 1) &
    (df['path_length'] > 8)
)
df.loc[malicious_filter, "label"] = 1
print(f"⚠️ Auto-labeled {malicious_filter.sum()} rows as malicious (label=1)")

# Reporting unlabeled entries
remaining_unlabeled = df['label'].isna().sum()
print(f"ℹ️ Remaining unlabeled entries: {remaining_unlabeled}")

# Saving file
df.to_csv(OUTPUT_CSV, index=False)
print(f"\n💾 Labeled dataset saved to: {OUTPUT_CSV}")
