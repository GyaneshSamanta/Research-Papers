import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, auc
import os

out_dir = "upgraded_visuals"
WORKING_DIR = "working datasets"

# RQ1 Table: Statistical Gap
df_acsi = pd.read_csv(f"{WORKING_DIR}/ACSI Data 2015.csv")
df_b2b = pd.read_csv(f"{WORKING_DIR}/system_ux_metrics_medium.csv")
target_col = 'Post_Task_Confidence'
if target_col not in df_b2b.columns: target_col = df_b2b.select_dtypes(include=np.number).columns[0]
raw_acsi = df_acsi['SATIS'].dropna()
raw_b2b = df_b2b[target_col].dropna()

min_b, max_b = raw_b2b.min(), raw_b2b.max()
if max_b <= 10: norm_b2b = (raw_b2b - min_b) / (max_b - min_b) * 100
else: norm_b2b = raw_b2b

mean_c = raw_acsi.mean()
mean_b = norm_b2b.mean()
stat, p_val = stats.mannwhitneyu(raw_acsi, norm_b2b)
n1, n2 = len(raw_acsi), len(norm_b2b)
var1, var2 = raw_acsi.var(), norm_b2b.var()
pooled_sd = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
cohens_d = (mean_c - mean_b) / pooled_sd

rq1_table = pd.DataFrame({
    'Metric': ['Consumer Mean Score', 'B2B Mean Score', 'Score Gap', 'P-Value', "Cohen's d (Effect Size)"],
    'Value': [f"{mean_c:.2f}", f"{mean_b:.2f}", f"{mean_c - mean_b:.2f}", f"{p_val:.5e}", f"{cohens_d:.2f}"]
})
rq1_table.to_csv(f"{out_dir}/table_rq1.csv", index=False)

# RQ2 Table: Efficiency Gain
df_manual = pd.read_csv(f"{WORKING_DIR}/Dataset_UI_Manual_Group.csv", header=1)
df_auto = pd.read_csv(f"{WORKING_DIR}/Dataset_UI_No_Manual_Group.csv", header=1)
def clean_ui(df, label):
    task_cols = [c for c in df.columns if str(c).replace('.', '').isdigit()]
    if not task_cols: task_cols = df.select_dtypes(include=['float64']).columns.tolist()
    df_long = df.melt(id_vars=[], value_vars=task_cols, var_name='Task_ID', value_name='Time_Seconds')
    return df_long.dropna()['Time_Seconds']

data_m = clean_ui(df_manual, 'Manual')
data_a = clean_ui(df_auto, 'Auto')

mean_m = data_m.mean()
mean_a = data_a.mean()
stat2, p_val2 = stats.ttest_ind(data_m, data_a, equal_var=False)
imp_pct = (mean_m - mean_a) / mean_m * 100

rq2_table = pd.DataFrame({
    'Metric': ['Avg Time - Complex UI (s)', 'Avg Time - Intuitive UI (s)', 'Time Saved (s)', 'Efficiency Gain (%)', 'P-Value'],
    'Value': [f"{mean_m:.2f}", f"{mean_a:.2f}", f"{mean_m - mean_a:.2f}", f"{imp_pct:.1f}%", f"{p_val2:.5e}"]
})
rq2_table.to_csv(f"{out_dir}/table_rq2.csv", index=False)

# RQ3 Table: Regional Adoption & Sales
df_usage = pd.read_csv(f"{WORKING_DIR}/feature_adoption_medium.csv")
df_sales = pd.read_csv(f"{WORKING_DIR}/SaaS Sales.csv")

mapping = {'US': 'AMER', 'EU': 'EMEA', 'ASIA': 'APJ', 'Other': 'EMEA'}
df_usage['Region_Clean'] = df_usage['Region'].astype(str).str.strip().map(mapping).fillna('AMER')
df_sales['Region_Clean'] = df_sales['Region'].astype(str).str.strip().str.upper()

df_usage['Is_Adopter'] = pd.to_numeric(df_usage['Feature_Used'], errors='coerce').fillna(0)
reg_usage = df_usage.groupby('Region_Clean').agg({'Engagement_Score': 'mean', 'Is_Adopter': 'mean'})
reg_sales = df_sales.groupby('Region_Clean').agg({'Sales': 'sum', 'Profit': 'sum'})
df_macro = pd.merge(reg_sales, reg_usage, on='Region_Clean', how='inner').reset_index()

df_macro['Adoption_Rate'] = (df_macro['Is_Adopter'] * 100).apply(lambda x: f"{x:.1f}%")
df_macro['Sales'] = df_macro['Sales'].apply(lambda x: f"${x:,.2f}")
df_macro['Avg_Engagement'] = df_macro['Engagement_Score'].apply(lambda x: f"{x:.2f}")

rq3_table = df_macro[['Region_Clean', 'Adoption_Rate', 'Avg_Engagement', 'Sales']]
rq3_table.columns = ['Region', 'Adoption Rate', 'Avg Engagement', 'Total Sales']
rq3_table.to_csv(f"{out_dir}/table_rq3.csv", index=False)
print("Tables generated.")
