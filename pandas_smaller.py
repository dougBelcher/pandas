# How do I make my pandas DataFrame smaller and faster?

import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(f'{drinks.columns}')
# Rtv information about the drinks df
# print(f'{drinks.info()}')
# force it to inspect the df
# print(f'{drinks.info(memory_usage="deep")}')
# print(f'{drinks.memory_usage()}')
# print(f'{drinks.memory_usage(deep=True)}')

# convert an object to integer
drinks["continent"] = drinks.continent.astype("category")
print(f'{drinks.dtypes}')
print(f'{drinks.head()}')
print(f'{drinks.continent.cat.codes.head()}')
