# L17 - What do I need to know about the pandas index? Part 1
# https://www.youtube.com/watch?v=OYZNk7Z9s6I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=17
# L18 - Part 2
# https://www.youtube.com/watch?v=15q-is8P_H4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=18

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
