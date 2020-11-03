# How do I read a tabular dta file into pandas?
# https://www.youtube.com/watch?v=5_QXMwezPJE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=2
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_table.html

import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders')

print(orders.head())

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)

print(users.head())
