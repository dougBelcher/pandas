# L11 - How do I use the axis parm
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.axes.html
# https://www.youtube.com/watch?v=PtO3t6ynH-8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=11

import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(f'{drinks.head()}')
print(f'\n{drinks.drop("continent", axis=1)}')      # axis='columns'
# print(f'{drinks.drop(2, axis=0)}')        # axis='index'
# print(f'{drinks.mean()}')
