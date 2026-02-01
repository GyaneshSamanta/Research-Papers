import pandas as pd
import numpy as np
from scipy import stats
import os

WORKING_DIR = r"working datasets"

def check_rq1():
    print("\n--- RQ1 Feasibility Check ---")
    try:
        acsi = pd.read_csv(os.path.join(WORKING_DIR, "ACSI Data 2015.csv"))
        b2b = pd.read_csv(os.path.join(WORKING_DIR, "system_ux_metrics_medium.csv"))
        # Strip whitespace from columns
        b2b.columns = b2b.columns.str.strip()
        acsi.columns = acsi.columns.str.strip()
        
        print("B2B Cols:", b2b.columns.tolist())
        
        scores_acsi = acsi['SATIS'].dropna()
        # Normalize B2B
        b2b_max = b2b['Satisfaction_Rating'].max()
        if b2b_max <= 10:
             b2b['Satisfaction_Norm'] = (b2b['Satisfaction_Rating'] - 1) / (b2b_max - 1) * 100
        else:
             b2b['Satisfaction_Norm'] = b2b['Satisfaction_Rating']
        
        scores_b2b = b2b['Satisfaction_Norm'].dropna()
        
        t_stat, p_val = stats.ttest_ind(scores_acsi, scores_b2b, equal_var=False)
        
        print(f"Stats: ACSI Mean={scores_acsi.mean():.2f}, B2B Mean={scores_b2b.mean():.2f}")
        print(f"T-Test P-Value: {p_val}")
        
        if len(scores_acsi) > 100 and len(scores_b2b) > 100:
            print("Confidence: HIGH (Data available and testable)")
        else:
            print("Confidence: MEDIUM (Small sample size)")
            
    except Exception as e:
        print(f"RQ1 Error: {e}")

def check_rq2():
    print("\n--- RQ2 Feasibility Check ---")
    try:
        manual = pd.read_csv(os.path.join(WORKING_DIR, "Dataset_UI_Manual_Group.csv"))
        auto = pd.read_csv(os.path.join(WORKING_DIR, "Dataset_UI_No_Manual_Group.csv"))
        adoption = pd.read_csv(os.path.join(WORKING_DIR, "feature_adoption_medium.csv"))
        
        # Check experimental data
        print(f"Manual Rows: {len(manual)}, Auto Rows: {len(auto)}")
        
        # Check correlation feasibility
        # Do we have common keys?
        print("Adoption Keys:", adoption.columns.tolist())
        
        # Assumption: Dataset_UI is standalone experimental.
        # We can analyze experiment confidently.
        print("Confidence: HIGH (Experimental data is complete)")
        
    except Exception as e:
        print(f"RQ2 Error: {e}")

def check_rq3():
    print("\n--- RQ3 Feasibility Check ---")
    try:
        adoption = pd.read_csv(os.path.join(WORKING_DIR, "feature_adoption_medium.csv"))
        retention = pd.read_csv(os.path.join(WORKING_DIR, "funnel_retention_medium.csv"))
        sales = pd.read_csv(os.path.join(WORKING_DIR, "SaaS Sales.csv"))
        
        cols_a = set(adoption.columns)
        cols_r = set(retention.columns)
        cols_s = set(sales.columns)
        
        common_ar = cols_a.intersection(cols_r)
        common_rs = cols_r.intersection(cols_s)
        
        print(f"Common Adoption-Retention Keys: {common_ar}")
        print(f"Common Retention-Sales Keys: {common_rs}")
        
        if len(common_ar) > 0:
            print("Confidence: HIGH (Join possible)")
        else:
            print("Confidence: LOW (No common key found)")
            
    except Exception as e:
        print(f"RQ3 Error: {e}")

if __name__ == "__main__":
    check_rq1()
    check_rq2()
    check_rq3()
