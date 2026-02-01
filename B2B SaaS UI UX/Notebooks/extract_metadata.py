import pandas as pd
import pyreadstat
import os
import glob

WORKING_DIR = r"working datasets"

def extract_metadata():
    files = glob.glob(os.path.join(WORKING_DIR, "*.sav"))
    with open(os.path.join(WORKING_DIR, "dataset_codebook.txt"), "w", encoding="utf-8") as out:
        for f in files:
            try:
                out.write(f"--- Metadata for {os.path.basename(f)} ---\n")
                df, meta = pyreadstat.read_sav(f)
                
                # Check variable labels
                labels = meta.column_names_to_labels
                for col, label in labels.items():
                    out.write(f"{col}: {label}\n")
                
                out.write("\n\n")
                print(f"Extracted metadata for {os.path.basename(f)}")
            except Exception as e:
                print(f"Error reading {f}: {e}")

if __name__ == "__main__":
    extract_metadata()
