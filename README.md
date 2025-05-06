# Low-Interaction Honeypot with Machine Learning Detection

This project is a low-interaction honeypot designed to detect and log HTTP-based attacks, such as directory brute-force scans and login attempts. It’s paired with a machine learning pipeline that classifies web traffic as benign or malicious using real honeypot-generated data.

## Project Structure
├── honeypot.py # Flask honeypot server

├── generateBenign.sh # Simulates benign traffic using curl

├── logs/
│ └── honeypot_logs.jsonl # Captured logs in JSON Lines format

├── parseLogs.py # Parses JSON logs → dataset.csv

├── labelData.py # Label dataset entries manually or via rules

├── unlabeled.py # Uses trained model to label remaining rows

├── labeled_dataset.csv # Final labeled dataset

├── trainModel.py # Trains and evaluates ML classifiers

├── compareModels.py # Visualizes model performance

├── model_comparison_chart.png

├── rf_confusion_matrix.png

└── README.md

## Getting Started

### 1. Install dependencies

```bash
pip install flask pandas scikit-learn matplotlib
```


### 2. Run Honeypot
```bash
python honeypot.py
```

### 3. Simulate Traffic
run benign traffic generator
```bash
bash generateBenign.sh
```
not included in directorym but install dirsearch and run dirsearch.py

### 4. Parse Logs
auto label based first
```bash
python parseLogs.py
```
then label remaining rows using trained model

```bash
python unlabeled.py
```
### 6. Train & Evaluate model
Running this will train logistic regression and random forest models, print performance metrics and save it as `labeeled_dataset.csv`

```bash
python trainModel.py
```

### 7. Visual Performance
```bash
python compareModels.py
```

Author:
Lorenz Wilkins — Computer Security Project
CU Denver, Spring 2025
