# How do I work with dates and times in pandas

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

ufo["Time"] = pd.to_datetime(ufo.Time)
# print(f'{ufo["Time"] = pd.to_datetime(ufo.Time)}')
# print(f'{ufo.head()}')
# print(f'{ufo.dtypes}')
# print(f'{ufo.Time.dt.hour}')
# print(f'{ufo.Time.dt.weekday_name}')      # Did not work
print(f'{ufo.Time.dt.dayofyear}')
