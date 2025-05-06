# Importing Packages
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load already labeled dataset
df = pd.read_csv("labeled_dataset.csv")

# Split data: labeled and unlabeled
labeled_df = df[df['label'].notna()]
unlabeled_df = df[df['label'].isna()]

# Features and labels from labeled portion
X_labeled = labeled_df.drop(columns=["label"])
y_labeled = labeled_df["label"]

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_labeled, y_labeled)

# Predict on unlabeled
X_unlabeled = unlabeled_df.drop(columns=["label"])
predicted_labels = rf.predict(X_unlabeled)

# Assign predictions to unlabeled rows
unlabeled_df["label"] = predicted_labels

# Combine and sort full dataset
fully_labeled_df = pd.concat([labeled_df, unlabeled_df]).sort_index()

# Save to file
fully_labeled_df.to_csv("fully_labeled_dataset.csv", index=False)
print("Saved fully labeled dataset to: fully_labeled_dataset.csv")
print(f"New rows labeled: {len(unlabeled_df)}")