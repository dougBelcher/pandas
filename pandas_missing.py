# How do I handle missing values in pandas?

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

# print the end of ufo; isnull(false/true; notnull(false/true
# print(f'{ufo.tail()}')
# print(f'{ufo.isnull().tail()}')
# print(f'{ufo.notnull().tail()}')

# print the columns and nbr of null rows
# print(f'{ufo.isnull().sum()}')

# drop rows with null data in a Series (how='any' is default, not needed can also be how='all')
# print(f'{ufo.dropna(how="any").shape}')

# drop rows with null data in a Series with a subset; only considers Series included
# print(f'{ufo.dropna(subset=["City", "Shape Reported"], how="any").shape}')
# print(f'{ufo["Shape Reported"].value_counts(dropna=False)}')

# Replace null data
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
print(f'{ufo["Shape Reported"]}')
