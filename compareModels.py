import matplotlib.pyplot as plt
import numpy as np

# Metric values from your test results
metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]
logreg_scores = [1.00, 1.00, 1.00, 1.00]
rf_scores = [1.00, 1.00, 1.00, 1.00]

x = np.arange(len(metrics))  # [0, 1, 2, 3]
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - width/2, logreg_scores, width, label='Logistic Regression')
bars2 = ax.bar(x + width/2, rf_scores, width, label='Random Forest')

# Labels and title
ax.set_ylabel('Score')
ax.set_ylim(0.0, 1.1)
ax.set_title('Model Performance Comparison')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# Add values on top of bars
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig("model_comparison_chart.png")
plt.show()
