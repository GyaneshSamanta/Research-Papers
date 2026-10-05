import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, auc, confusion_matrix

# Styling for Publication Quality
plt.style.use('seaborn-v0_8-paper')
sns.set_context("talk", font_scale=1.1)
pd.set_option('display.float_format', '{:.2f}'.format)

print("Libraries & Modelling Toolkit Loaded.")

WORKING_DIR = r"..\working datasets"

try:
    df_acsi = pd.read_csv(f"{WORKING_DIR}\\ACSI Data 2015.csv")
    df_b2b = pd.read_csv(f"{WORKING_DIR}\\system_ux_metrics_medium.csv")
except FileNotFoundError:
    WORKING_DIR = r"working datasets"
    df_acsi = pd.read_csv(f"{WORKING_DIR}\\ACSI Data 2015.csv")
    df_b2b = pd.read_csv(f"{WORKING_DIR}\\system_ux_metrics_medium.csv")

# Metric Alignment
# ACSI uses 'SATIS' (0-100)
# B2B uses 'Post_Task_Confidence' (Likert 1-5 or similar)

target_col = 'Post_Task_Confidence'
if target_col not in df_b2b.columns:
    # Fallback to first numeric if specific Col missing (Robustness)
    target_col = df_b2b.select_dtypes(include=np.number).columns[0]

raw_acsi = df_acsi['SATIS'].dropna()
raw_b2b = df_b2b[target_col].dropna()

# Normalize B2B to 0-100 Scale
min_b, max_b = raw_b2b.min(), raw_b2b.max()
if max_b <= 10:
    print(f"Normalizing B2B ({min_b}-{max_b}) -> (0-100)")
    norm_b2b = (raw_b2b - min_b) / (max_b - min_b) * 100
else:
    norm_b2b = raw_b2b

# Consolidate for Modelling
df_model = pd.DataFrame({
    'Score': np.concatenate([raw_acsi, norm_b2b]),
    'Source': ['Consumer'] * len(raw_acsi) + ['B2B'] * len(norm_b2b),
    'Is_B2B': [0] * len(raw_acsi) + [1] * len(norm_b2b) # Target for Logistic Regression
})

print(f"Data Processed. Total Samples: {len(df_model)}")

plt.figure(figsize=(12, 7))

# KDE Plot (Smooth Density)
sns.kdeplot(data=df_model, x='Score', hue='Source', fill=True, palette={'Consumer': '#3498db', 'B2B': '#e74c3c'}, alpha=0.4, linewidth=2)

# Mean Lines
mean_c = df_model[df_model['Source']=='Consumer']['Score'].mean()
mean_b = df_model[df_model['Source']=='B2B']['Score'].mean()

plt.axvline(mean_c, color='#3498db', linestyle='--', label=f'Consumer Mean ({mean_c:.1f})')
plt.axvline(mean_b, color='#e74c3c', linestyle='--', label=f'B2B Mean ({mean_b:.1f})')

plt.title("The Gap: Consumer Expectations dist. vs B2B Reality dist.", fontsize=16, fontweight='bold')
plt.xlabel("Satisfaction Score (Normalized 0-100)")
plt.xlim(0, 100)
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
sns.ecdfplot(data=df_model, x='Score', hue='Source', palette={'Consumer': '#3498db', 'B2B': '#e74c3c'}, linewidth=3)
plt.axvline(mean_c, color='gray', linestyle=':', label='Avg Consumer Score')
plt.title("CDF: Cumulative Performance Lag", fontsize=16)
plt.ylabel("Cumulative Probability")
plt.legend()
plt.show()

# Logistic Regression: Predict 'Is_B2B' from 'Score'
X = df_model[['Score']]
y = df_model['Is_B2B']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Metrics
report = classification_report(y_test, y_pred, output_dict=True)
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# ROC Curve Visualization
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Chance (No Gap)')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Modelling the Gap: Can Score Predict Platform Type?')
plt.legend(loc="lower right")
plt.show()

print("--- Model Report ---")
print(f"Model Accuracy: {report['accuracy']:.2%}")
print(f"ROC-AUC Score:  {roc_auc:.2f}")

stat, p_val = stats.mannwhitneyu(raw_acsi, norm_b2b)

# Cohen's d
n1, n2 = len(raw_acsi), len(norm_b2b)
var1, var2 = raw_acsi.var(), norm_b2b.var()
pooled_sd = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
cohens_d = (mean_c - mean_b) / pooled_sd

print(f"Results:\nMean Gap: {mean_c - mean_b:.2f} points")
print(f"P-Value:  {p_val:.5e}")
print(f"Cohen's d: {cohens_d:.2f}")

result = "SIGNIFICANT" if p_val < 0.05 else "NOT SIGNIFICANT"
magnitude = "LARGE" if abs(cohens_d) > 0.8 else ("MEDIUM" if abs(cohens_d) > 0.5 else "SMALL")

print(f"\nFINAL CONCLUSION: The gap is {result} with a {magnitude} effect size.")

