# How do I select multiple rows and columns from a pandas DataFrame?

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(f'{ufo.columns}')

# print the first row and all columns
# print(f'{ufo.loc[0 , :]}')

# print first three rows and all columns
# print(f'{ufo.loc[[0, 1, 2], :]}')

# SAA
# print(f'{ufo.loc[0:2, :]}')

# SAA (not pythonic)
# print(f'{ufo.loc[0:2]}')

# Rtv all rows and city & state columns
# print(f'{ufo.loc[:, ["City", "State"]]}')

# Rtv all rows and columns city thru  (w/o Time), inclusive of both sides
# print(f'loc method:')
# print(f'{ufo.loc[:, "City":"State"]}')
#
# # Rtv SAA differently
# print(f'head method:')
# print(f'{ufo.head(3).drop("Time", axis=1)}')

# use loc to rtv only the rows w/ city Oakland
# print(f'{ufo.loc[ufo.City=="Oakland", :]}')

# Rtv using iloc (integer position)
# print(f'{ufo.iloc[:, [0, 3]]}')

# Rtv using iloc (integer position) inclusive of the first number; exclusive of the second
# print(f'{ufo.iloc[:, 0:4]}')

# Not recommended shortcuts
# print(f'{ufo[["City", "State"]]}')              # refers to all rows and two columns
# print(f'{ufo[0:2]}')                            # refers to rows and all columns
# Preferred
# print(f'{ufo.loc[:, ["City", "State"]]}')       # refers to all rows and two columns
# print(f'{ufo.iloc[0:2, :]}')                    # refers to rows and all columns

drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')
print(f'{drinks.columns}')
print(f'{drinks.head()}')
# print(f'{drinks.ix["Albania", 0]}')           # does not currently work
