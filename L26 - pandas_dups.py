# L26 - How do I find and remove duplicate rows in pandas?
# https://www.youtube.com/watch?v=ht5buXUMqkQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=26

import pandas as pd

# read a dataset of movie reviewers (mofiying the default parm values for read_table
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')

print(f'{users.head()}')
# print(f'{users.zip_code.duplicated().sum()}')             # Series method
# print(f'{users.duplicated().sum()}')                      # dataFrame
# print(f'{users.loc[users.duplicated()]}')
# print(f'{users.drop_duplicates(keep="first")}')

print(f'{users.drop_duplicates(subset=["age", "zip_code"]).shape}')
