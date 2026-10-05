import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter, CoxPHFitter
from scipy import stats

# Statistical Plotting Style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("talk", font_scale=1.1)
pd.set_option('display.float_format', '{:.2f}'.format)

print("Libraries Loaded.")

WORKING_DIR = r"..\working datasets"
try:
    df_usage = pd.read_csv(f"{WORKING_DIR}\\feature_adoption_medium.csv")
    df_sales = pd.read_csv(f"{WORKING_DIR}\\SaaS Sales.csv")
except FileNotFoundError:
    WORKING_DIR = r"working datasets"
    df_usage = pd.read_csv(f"{WORKING_DIR}\\feature_adoption_medium.csv")
    df_sales = pd.read_csv(f"{WORKING_DIR}\\SaaS Sales.csv")

# --- 1. Fix Region Mismatch ---
# Usage has: [US, EU, ASIA]
# Sales has: [AMER, EMEA, APJ]
mapping = {
    'US': 'AMER',
    'EU': 'EMEA',
    'ASIA': 'APJ',
    'Other': 'EMEA' # Assumption for 'Other' to preserve data
}

df_usage['Region_Clean'] = df_usage['Region'].astype(str).str.strip().map(mapping).fillna('AMER') # Fallback to biggest market
df_sales['Region_Clean'] = df_sales['Region'].astype(str).str.strip().str.upper()
print("Region Mapping Applied.")

# --- 2. Fix Qualitative Churn Logic ---
# Subscription_Status found as floats [0.0, 1.0]. Assuming 0 = Churned/Inactive.
if 'Subscription_Status' in df_usage.columns:
    df_usage['Churn_Event'] = df_usage['Subscription_Status'].fillna(0).apply(lambda x: 1 if x == 0 else 0)
else:
    df_usage['Churn_Event'] = df_usage['Retention_Day_30'].fillna(0).apply(lambda x: 1 if x < 20 else 0)

print(f"User Sample: {len(df_usage)}. Observed Churn Events: {df_usage['Churn_Event'].sum()}")

# Prepare Tenure
df_usage['Tenure_Days'] = pd.to_numeric(df_usage['Days_Since_Launch'], errors='coerce').fillna(1)
df_usage['Is_Adopter'] = pd.to_numeric(df_usage['Feature_Used'], errors='coerce').fillna(0)

kmf = KaplanMeierFitter()
plt.figure(figsize=(10, 6))

# Plot Adopters (1)
mask_a = (df_usage['Is_Adopter'] == 1)
kmf.fit(df_usage[mask_a]['Tenure_Days'], event_observed=df_usage[mask_a]['Churn_Event'], label='Adopters')
kmf.plot_survival_function(color='green', linewidth=3, ci_show=False)

# Plot Non-Adopters (0)
mask_n = (df_usage['Is_Adopter'] == 0)
kmf.fit(df_usage[mask_n]['Tenure_Days'], event_observed=df_usage[mask_n]['Churn_Event'], label='Non-Adopters')
kmf.plot_survival_function(color='red', linewidth=3, ci_show=False)

plt.title("Survival Analysis: Adoption vs Retention Span")
plt.ylabel("Survival Probability")
plt.xlabel("Days Active")
plt.show()

# Prepare Clean Dataset for Cox
cox_df = df_usage[['Tenure_Days', 'Churn_Event', 'Is_Adopter', 'Engagement_Score']].dropna()

try:
    # Penalizer=0.5 handles collinearity/matrix inversion issues
    cph = CoxPHFitter(penalizer=0.5)
    cph.fit(cox_df, duration_col='Tenure_Days', event_col='Churn_Event')
    
    cph.print_summary()
    
    print("\n--- Interpretation ---")
    print("HR < 1.0 = Protective (Feature usage reduces churn).")
    print("HR > 1.0 = Risky (Feature usage increases churn).")
except Exception as e:
    print(f"Model Error: {e}")

# Aggregating Usage
reg_usage = df_usage.groupby('Region_Clean').agg({
    'Engagement_Score': 'mean',
    'Is_Adopter': 'mean' # % Adoption Penetration
}).rename(columns={'Engagement_Score': 'Avg_Engagement', 'Is_Adopter': 'Adoption_Rate'})

# Aggregating Sales
reg_sales = df_sales.groupby('Region_Clean').agg({
    'Sales': 'sum',
    'Profit': 'sum'
})

# Merge using Cleaned Keys
df_macro = pd.merge(reg_sales, reg_usage, on='Region_Clean', how='inner')

print(f"Matched Regions: {len(df_macro)}")
display(df_macro)

if len(df_macro) >= 2:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df_macro, x='Adoption_Rate', y='Sales', s=200, hue='Region_Clean', palette='viridis')
    plt.title("Does Regional Adoption Drive Sales?")
    plt.xlabel("Feature Adoption Rate (Penetration)")
    plt.ylabel("Total Regional Sales")
    plt.grid(True)
    plt.show()
else:
    print("Not enough regional overlap for scatter plot.")

