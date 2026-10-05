import json
import glob

for nb_file in glob.glob("MainNotebook/*_Refined.ipynb"):
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    code = ""
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            code += "".join(cell['source']) + "\n\n"
    py_file = nb_file.replace('.ipynb', '.py')
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Extracted {py_file}")
