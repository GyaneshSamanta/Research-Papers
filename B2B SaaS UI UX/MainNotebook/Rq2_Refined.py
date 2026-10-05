import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# Scientific Plotting Style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("talk", font_scale=1.1)
pd.set_option('display.float_format', '{:.2f}'.format)

print("Libraries Loaded.")

WORKING_DIR = r"..\working datasets"
try:
    df_manual = pd.read_csv(f"{WORKING_DIR}\\Dataset_UI_Manual_Group.csv", header=1)
    df_auto = pd.read_csv(f"{WORKING_DIR}\\Dataset_UI_No_Manual_Group.csv", header=1)
except FileNotFoundError:
    WORKING_DIR = r"working datasets"
    df_manual = pd.read_csv(f"{WORKING_DIR}\\Dataset_UI_Manual_Group.csv", header=1)
    df_auto = pd.read_csv(f"{WORKING_DIR}\\Dataset_UI_No_Manual_Group.csv", header=1)

# Data Cleaning
def clean_ui_data(df, label):
    task_cols = [c for c in df.columns if str(c).replace('.', '').isdigit()]
    if not task_cols: task_cols = df.select_dtypes(include=['float64']).columns.tolist()
    
    df_long = df.melt(id_vars=[], value_vars=task_cols, var_name='Task_ID', value_name='Time_Seconds')
    df_long['Group'] = label
    return df_long.dropna()

data_m = clean_ui_data(df_manual, 'Manual (Complex)')
data_a = clean_ui_data(df_auto, 'No Manual (Intuitive)')
df_exp = pd.concat([data_m, data_a], ignore_index=True)

print(f"Experiment Data Loaded. N={len(df_exp)}")

plt.figure(figsize=(10, 6))
# Using list palette is safer than dict keys
sns.violinplot(data=df_exp, x='Group', y='Time_Seconds', hue='Group', palette=['#e74c3c', '#2ecc71'])
plt.title("Impact of Intuitive Design on Task Efficiency")
plt.show()

stat, p_val = stats.ttest_ind(data_m['Time_Seconds'], data_a['Time_Seconds'], equal_var=False)
imp_pct = (data_m['Time_Seconds'].mean() - data_a['Time_Seconds'].mean()) / data_m['Time_Seconds'].mean() * 100

print(f"T-Test P-Value: {p_val:.5e}")
print(f"Efficiency Gain: {imp_pct:.1f}%")
if p_val < 0.05: print("Conclusion: Statistically Significant Efficiency Gain.")

df_adopt = pd.read_csv(f"{WORKING_DIR}\\feature_adoption_medium.csv")

# --- CRITICAL DATA CLEANING ---
# 1. Force Numeric Conversion
df_adopt['Adopted'] = pd.to_numeric(df_adopt['Feature_Used'], errors='coerce')

# 2. Drop NaNs
df_clean = df_adopt.dropna(subset=['Engagement_Score', 'Adopted']).copy()

# 3. Cast to integer for readability
df_clean['Adopted'] = df_clean['Adopted'].astype(int)
df_clean['Adopted_Label'] = df_clean['Adopted'].map({0: 'Not Adopted', 1: 'Adopted'})

print("Class Distribution:\n", df_clean['Adopted_Label'].value_counts())
variance_ok = len(df_clean['Adopted'].unique()) > 1

if variance_ok:
    plt.figure(figsize=(8, 6))
    # SAFE PLOTTING: Uses 'Adopted_Label' (string) and list-palette to avoid KeyErrors
    sns.boxplot(data=df_clean, x='Adopted_Label', y='Engagement_Score', 
                order=['Not Adopted', 'Adopted'], 
                palette=['#95a5a6', '#3498db'])
    plt.title("Engagement Score vs Adoption Status")
    plt.show()
else:
    print("Error: Not enough data variance to plot.")

if variance_ok:
    X = df_clean[['Engagement_Score']]
    y = df_clean['Adopted']
    
    logit = sm.Logit(y, sm.add_constant(X)).fit(disp=0)
    
    odds = np.exp(logit.params['Engagement_Score'])
    p = logit.pvalues['Engagement_Score']
    
    print(f"\nOdds Ratio: {odds:.2f} (P={p:.5e})")
    if p < 0.05:
        print(f"CONCLUSION: Significant. +1 Engagement Score = {(odds-1)*100:.1f}% higher Adoption Probability.")

