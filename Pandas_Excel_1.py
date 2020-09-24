# Pandas_Excel_1.py
import pandas as pd
import os

os.chdir('/Users/Doug/PycharmProjects/Basic/Excel')
os.makedirs('Excel', exist_ok=True)

excel_file_path = 'training_status.xlsx'

df = pd.read_excel(excel_file_path)
print(df)

split_values = df['Shift'].unique()
# print(split_values)
#
# for value in split_values:
#     df1 = df[df['Shift'] == value]
#     output_file_name = "Shift_" + str(value) + "_Training.xlsx"
#     df1.to_excel(output_file_name, index=False)
