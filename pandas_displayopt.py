# How do i change display options in pandas?
# https://www.youtube.com/watch?v=yiO43TQ4xvc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=28

import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

# print(f'{drinks}')

# print(f'{pd.get_option("display.max_rows")}')       # prints max_rows before
# pd.set_option('display.max_rows', None)             # prints all rows
# print(f'{pd.get_option("display.max_rows")}')       # prints max_rows after
# pd.reset_option('display.max_rows')                 # reset back to default

# print(f'{pd.get_option("display.max_columns")}')
# pd.set_option('display.max_columns', None)
# print(f'{pd.get_option("display.max_columns")}')
# pd.reset_option('display.max_columns')
# print(f'{drinks}')

# train = pd.read_csv('http://bit.ly/kaggletrain')
# print(f'{train.head()}')

# print(f'{pd.get_option("display.max_colwidth")}')
# print(f'{pd.get_option("display.precision")}')
# pd.set_option('display.precision', 2)
# print(f'{pd.get_option("display.precision")}')
# print(f'{train.head()}')

# pd.set_option('display.float_format', '{:,}'.format)        # only affects float columns

# print(f'{pd.describe_option()}')                            # display all pandas options
# print(f'{pd.describe_option("row")}')                       # display all pandas options w/ row
# print(f'{pd.describe_option("display")}')                       # display all pandas options w/ display

pd.reset_option('all')                                        # reset all options
