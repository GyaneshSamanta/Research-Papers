import pandas as pd
import os

WORKING_DIR = r"working datasets"
# Datasets that had score 0 or low score
targets = ["B2B Marketing Dataset.csv", "Dataset_UI.csv", "ACSI Data 2015.csv"] 

# Check if ACSI converted?
# I see .sav and .xlsx in previous lists. I need to make sure I converted them.
# The user said I converted .sav into .xlsx (actually I converted to .csv).
# I'll check all csvs.

def inspect_datasets():
    print("Manual Inspection of Low-Score Datasets:\n")
    for t in targets:
        path = os.path.join(WORKING_DIR, t)
        if os.path.exists(path):
            try:
                print(f"--- {t} ---")
                df = pd.read_csv(path, nrows=2)
                print(list(df.columns))
                print("\n")
            except Exception as e:
                print(f"Error reading {t}: {e}")
        else:
             # Try checking if there is an xlsx or sav that wasn't converted?
             # I ran conversion on all .sav and .xlsx in working datasets.
             # Did I move ACSI to working datasets?
             print(f"File {t} not found in working datasets.")

    # Amos check
    amos_path = os.path.join(WORKING_DIR, "F929679E18.AmosP")
    if os.path.exists(amos_path):
        print(f"--- F929679E18.AmosP ---")
        try:
            with open(amos_path, 'rb') as f:
                header = f.read(100)
                print(f"Header: {header}")
        except Exception as e:
            print(f"Error reading AmosP: {e}")

if __name__ == "__main__":
    inspect_datasets()
