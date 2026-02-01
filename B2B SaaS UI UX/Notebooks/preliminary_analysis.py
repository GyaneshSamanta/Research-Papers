import pandas as pd
import os
import glob

WORKING_DIR = r"working datasets"

UX_KEYWORDS = ['ux', 'user', 'experience', 'ease', 'satisfaction', 'score', 'rating', 'time', 'usability', 'design', 'interface', 'sus', 'ces', 'task']
BIZ_KEYWORDS = ['revenue', 'churn', 'retention', 'sales', 'cost', 'conversion', 'adoption', 'customer', 'clv', 'nrr', 'cac', 'ltv', 'profit']

def analyze_datasets():
    print("Analyzying Datasets for Relevance...\n")
    files = glob.glob(os.path.join(WORKING_DIR, "*.csv"))
    
    relevance_report = []

    for f in files:
        fname = os.path.basename(f)
        try:
            df = pd.read_csv(f, nrows=5) # Read partial to get columns
            cols = [c.lower() for c in df.columns]
            
            ux_matches = [c for c in cols if any(k in c for k in UX_KEYWORDS)]
            biz_matches = [c for c in cols if any(k in c for k in BIZ_KEYWORDS)]
            
            score = len(ux_matches) + len(biz_matches)
            
            report = {
                "file": fname,
                "ux_cols": ux_matches[:5], # Limit output
                "biz_cols": biz_matches[:5],
                "score": score,
                "total_cols": len(cols)
            }
            relevance_report.append(report)
            
        except Exception as e:
            print(f"Error reading {fname}: {e}")

    # Sort by score
    relevance_report.sort(key=lambda x: x['score'], reverse=True)

    for r in relevance_report:
        print(f"--- {r['file']} (Score: {r['score']}) ---")
        print(f"  UX Matches: {r['ux_cols']}")
        print(f"  Biz Matches: {r['biz_cols']}")
        print(f"  Total Cols: {r['total_cols']}")
        print("")

if __name__ == "__main__":
    analyze_datasets()
