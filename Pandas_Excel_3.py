# Pandas_Excel_3.py
# Easy Spreadsheet Data Analyis Methods

import pandas as pd

excel_file_path = 'Excel/Weight.xlsx'

df = pd.read_excel(excel_file_path)
print(df.columns)
