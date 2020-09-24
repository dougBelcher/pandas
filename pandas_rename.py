# How do I rename columns in a pandas dataframe

import pandas as pd

# ufo = pd.read_csv('http://bit.ly/uforeports')
# print(f'{ufo.columns}')
# ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)
# print(f'{ufo.columns}')

ufo_cols = ('city', 'colors reported', 'shape reported', 'state', 'time')
# ufo.columns = ufo_cols
# print(f'{ufo.columns}')

ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols, header=0)
print(f'{ufo.columns}')

ufo.columns = ufo.columns.str.replace(' ', '_')
print(f'{ufo.columns}')

