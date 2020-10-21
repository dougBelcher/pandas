# L5 - How do I rename columns in a pandas dataframe
# https://www.youtube.com/watch?v=0uBirYFhizE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=5

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

