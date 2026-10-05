import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import statsmodels.api as sm
from lifelines import KaplanMeierFitter
import os

# Create output directory
out_dir = "upgraded_visuals"
os.makedirs(out_dir, exist_ok=True)

# Aesthetic Guidelines for Academic Papers
plt.style.use('seaborn-v0_8-paper')
sns.set_theme(style="whitegrid", palette="colorblind", context="paper", font_scale=1.3)
plt.rcParams.update({
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'font.family': 'sans-serif',
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})

WORKING_DIR = "working datasets"

# =======================
# RQ1 Visualizations
# =======================
df_acsi = pd.read_csv(f"{WORKING_DIR}/ACSI Data 2015.csv")
df_b2b = pd.read_csv(f"{WORKING_DIR}/system_ux_metrics_medium.csv")

target_col = 'Post_Task_Confidence'
if target_col not in df_b2b.columns:
    target_col = df_b2b.select_dtypes(include=np.number).columns[0]

raw_acsi = df_acsi['SATIS'].dropna()
raw_b2b = df_b2b[target_col].dropna()

min_b, max_b = raw_b2b.min(), raw_b2b.max()
if max_b <= 10:
    norm_b2b = (raw_b2b - min_b) / (max_b - min_b) * 100
else:
    norm_b2b = raw_b2b

df_model = pd.DataFrame({
    'Score': np.concatenate([raw_acsi, norm_b2b]),
    'Source': ['Consumer'] * len(raw_acsi) + ['B2B'] * len(norm_b2b),
    'Is_B2B': [0] * len(raw_acsi) + [1] * len(norm_b2b)
})

# 1. KDE Plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df_model, x='Score', hue='Source', fill=True, alpha=0.5, linewidth=2, ax=ax)
mean_c = df_model[df_model['Source']=='Consumer']['Score'].mean()
mean_b = df_model[df_model['Source']=='B2B']['Score'].mean()
ax.axvline(mean_c, color=sns.color_palette("colorblind")[0], linestyle='--', label=f'Consumer Mean ({mean_c:.1f})')
ax.axvline(mean_b, color=sns.color_palette("colorblind")[1], linestyle='--', label=f'B2B Mean ({mean_b:.1f})')
ax.set_title("Distribution Gap: Consumer Expectations vs. B2B Reality")
ax.set_xlabel("Satisfaction Score (Normalized 0-100)")
ax.set_ylabel("Density")
ax.set_xlim(0, 100)
ax.legend()
plt.tight_layout()
plt.savefig(f"{out_dir}/RQ1_Fig1_KDE_Gap.png")
plt.close()

# 2. ECDF Plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.ecdfplot(data=df_model, x='Score', hue='Source', linewidth=3, ax=ax)
ax.axvline(mean_c, color='gray', linestyle=':', label='Avg Consumer Score')
ax.set_title("Cumulative Distribution: Performance Lag in B2B")
ax.set_xlabel("Satisfaction Score (Normalized 0-100)")
ax.set_ylabel("Cumulative Probability")
ax.legend()
plt.tight_layout()
plt.savefig(f"{out_dir}/RQ1_Fig2_ECDF_Lag.png")
plt.close()

# 3. ROC Curve
X = df_model[['Score']]
y = df_model['Is_B2B']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(fpr, tpr, color=sns.color_palette("colorblind")[3], lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Chance')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('Predictive Power of Satisfaction Score for Platform Type')
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(f"{out_dir}/RQ1_Fig3_ROC_Curve.png")
plt.close()

# =======================
# RQ2 Visualizations
# =======================
df_manual = pd.read_csv(f"{WORKING_DIR}/Dataset_UI_Manual_Group.csv", header=1)
df_auto = pd.read_csv(f"{WORKING_DIR}/Dataset_UI_No_Manual_Group.csv", header=1)

def clean_ui_data(df, label):
    task_cols = [c for c in df.columns if str(c).replace('.', '').isdigit()]
    if not task_cols: task_cols = df.select_dtypes(include=['float64']).columns.tolist()
    df_long = df.melt(id_vars=[], value_vars=task_cols, var_name='Task_ID', value_name='Time_Seconds')
    df_long['Group'] = label
    return df_long.dropna()

data_m = clean_ui_data(df_manual, 'Manual (Complex)')
data_a = clean_ui_data(df_auto, 'No Manual (Intuitive)')
df_exp = pd.concat([data_m, data_a], ignore_index=True)

# 4. Violin Plot
fig, ax = plt.subplots(figsize=(9, 6))
sns.violinplot(data=df_exp, x='Group', y='Time_Seconds', hue='Group', palette="colorblind", inner="quartile", ax=ax, legend=False)
ax.set_title("Impact of Intuitive Design on Task Efficiency")
ax.set_xlabel("Design Interface Type")
ax.set_ylabel("Task Completion Time (Seconds)")
plt.tight_layout()
plt.savefig(f"{out_dir}/RQ2_Fig1_Violin_Efficiency.png")
plt.close()

df_adopt = pd.read_csv(f"{WORKING_DIR}/feature_adoption_medium.csv")
df_adopt['Adopted'] = pd.to_numeric(df_adopt['Feature_Used'], errors='coerce')
df_clean = df_adopt.dropna(subset=['Engagement_Score', 'Adopted']).copy()
df_clean['Adopted'] = df_clean['Adopted'].astype(int)
df_clean['Adopted_Label'] = df_clean['Adopted'].map({0: 'Not Adopted', 1: 'Adopted'})

# 5. Boxplot
if len(df_clean['Adopted'].unique()) > 1:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df_clean, x='Adopted_Label', y='Engagement_Score', order=['Not Adopted', 'Adopted'], palette="colorblind", hue='Adopted_Label', legend=False, ax=ax)
    ax.set_title("Engagement Score vs. Feature Adoption Status")
    ax.set_xlabel("Adoption Status")
    ax.set_ylabel("User Engagement Score")
    plt.tight_layout()
    plt.savefig(f"{out_dir}/RQ2_Fig2_Boxplot_Adoption.png")
    plt.close()

# =======================
# RQ3 Visualizations
# =======================
df_usage = pd.read_csv(f"{WORKING_DIR}/feature_adoption_medium.csv")
df_sales = pd.read_csv(f"{WORKING_DIR}/SaaS Sales.csv")

mapping = {'US': 'AMER', 'EU': 'EMEA', 'ASIA': 'APJ', 'Other': 'EMEA'}
df_usage['Region_Clean'] = df_usage['Region'].astype(str).str.strip().map(mapping).fillna('AMER')
df_sales['Region_Clean'] = df_sales['Region'].astype(str).str.strip().str.upper()

if 'Subscription_Status' in df_usage.columns:
    df_usage['Churn_Event'] = df_usage['Subscription_Status'].fillna(0).apply(lambda x: 1 if x == 0 else 0)
else:
    df_usage['Churn_Event'] = df_usage['Retention_Day_30'].fillna(0).apply(lambda x: 1 if x < 20 else 0)

df_usage['Tenure_Days'] = pd.to_numeric(df_usage['Days_Since_Launch'], errors='coerce').fillna(1)
df_usage['Is_Adopter'] = pd.to_numeric(df_usage['Feature_Used'], errors='coerce').fillna(0)

# 6. Kaplan Meier
kmf = KaplanMeierFitter()
fig, ax = plt.subplots(figsize=(10, 6))
mask_a = (df_usage['Is_Adopter'] == 1)
kmf.fit(df_usage[mask_a]['Tenure_Days'], event_observed=df_usage[mask_a]['Churn_Event'], label='Adopters')
kmf.plot_survival_function(ax=ax, color=sns.color_palette("colorblind")[2], linewidth=3, ci_show=True)

mask_n = (df_usage['Is_Adopter'] == 0)
kmf.fit(df_usage[mask_n]['Tenure_Days'], event_observed=df_usage[mask_n]['Churn_Event'], label='Non-Adopters')
kmf.plot_survival_function(ax=ax, color=sns.color_palette("colorblind")[3], linewidth=3, ci_show=True)

ax.set_title("Survival Analysis: Feature Adoption vs. Customer Retention")
ax.set_ylabel("Survival Probability")
ax.set_xlabel("Days Active (Tenure)")
plt.tight_layout()
plt.savefig(f"{out_dir}/RQ3_Fig1_Survival_Curve.png")
plt.close()

# 7. Scatterplot
reg_usage = df_usage.groupby('Region_Clean').agg({'Engagement_Score': 'mean', 'Is_Adopter': 'mean'}).rename(columns={'Engagement_Score': 'Avg_Engagement', 'Is_Adopter': 'Adoption_Rate'})
reg_sales = df_sales.groupby('Region_Clean').agg({'Sales': 'sum', 'Profit': 'sum'})
df_macro = pd.merge(reg_sales, reg_usage, on='Region_Clean', how='inner')

if len(df_macro) >= 2:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df_macro, x='Adoption_Rate', y='Sales', s=250, hue='Region_Clean', palette="colorblind", ax=ax)
    ax.set_title("Regional Feature Adoption vs. Total Sales")
    ax.set_xlabel("Feature Adoption Rate (Penetration)")
    ax.set_ylabel("Total Regional Sales (USD)")
    plt.tight_layout()
    plt.savefig(f"{out_dir}/RQ3_Fig2_Scatter_Sales.png")
    plt.close()

print("All visuals generated successfully.")
