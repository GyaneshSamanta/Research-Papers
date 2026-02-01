import pandas as pd
import os
import glob

# distinct paths usually but here they are relative
WORKING_DIR = r"working datasets"

def convert_sav_to_csv():
    files = glob.glob(os.path.join(WORKING_DIR, "*.sav"))
    for f in files:
        try:
            print(f"Converting {f}...")
            # pyreadstat is used by read_spss
            df = pd.read_spss(f)
            new_name = f.replace(".sav", ".csv")
            df.to_csv(new_name, index=False)
            print(f"Saved {new_name}")
        except Exception as e:
            print(f"Error converting {f}: {e}")

def convert_xlsx_to_csv():
    files = glob.glob(os.path.join(WORKING_DIR, "*.xlsx"))
    for f in files:
        try:
            print(f"Converting {f}...")
            # Load ExcelFile to get sheet names
            xl = pd.ExcelFile(f)
            for sheet in xl.sheet_names:
                df = pd.read_excel(f, sheet_name=sheet)
                # Append sheet name to filename
                base_name = f.replace(".xlsx", "")
                safe_sheet = sheet.replace(" ", "_")
                new_name = f"{base_name}_{safe_sheet}.csv"
                df.to_csv(new_name, index=False)
                print(f"Saved {new_name}")
        except Exception as e:
            print(f"Error converting {f}: {e}")

if __name__ == "__main__":
    print("Starting preprocessing...")
    convert_sav_to_csv()
    convert_xlsx_to_csv()
    print("Preprocessing completed.")
