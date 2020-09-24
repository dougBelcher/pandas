# Pandas_Excel_2.py
# Reading data from Weight Excel
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

import pandas as pd

pd.set_option('display.precision', 2)

# excel_file_path = 'Weight.xlsx'
# weight = pd.read_excel(excel_file_path)
weight = pd.read_excel('/Users/Doug/Documents/My Dropbox/Doug/weight.xlsx', sheet_name='Weekly')

print(f'{weight}')
