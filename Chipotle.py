# Read tabular data file - Chipotle

import pandas as pd

# orders = pd.read_table("http://bit.ly/chiporders")
# print(f"{orders}")

users = pd.read_table('http://bit.ly/movieusers')
print(f'{users}')

user_columns = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_columns)
print(f"{users}")