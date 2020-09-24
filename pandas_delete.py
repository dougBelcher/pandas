# How do I remove columns from a pandas dataframe
# https://www.youtube.com/watch?v=gnUKkS964WQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=6

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(f'{ufo.columns}')
ufo.drop(['Colors Reported', 'State'], axis=1, inplace=True)            # dataframe
# print(f'{ufo.columns}')
# print(f'{ufo}')

ufo = pd.read_csv('http://bit.ly/uforeports')
print(f'{ufo}')
ufo.drop([0, 1], axis=0, inplace=True)
print(f'{ufo}')
