# What do I need to know about the pandas index?

import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
# print(f'{drinks.index}')

# print(f'{drinks.loc[23, "beer_servings"]}')

# replace the index
drinks.set_index('country', inplace=True)
# print(f'{drinks}')

# print(f'{drinks.loc["Brazil", "beer_servings"]}')

# Put the index back
# drinks.reset_index(inplace=True)
# print(f'{drinks}')

people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')
print(f'{people}')

print(f'{drinks.beer_servings * people}')

print(f'{pd.concat([drinks, people], axis=1).head()}')
