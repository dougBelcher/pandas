# When should I use a "groupby" in pandas?

import pandas as pd

# drinks by country from the bit.ly link
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
# print(f'{drinks.head()}')

# print the mean of all the rows
# print(f'{drinks.beer_servings.mean()}')

# use groupby by continent
# print(f'{drinks.groupby("continent").beer_servings.mean()}')

# only select the drinks for Africa and show mean
# print(f'{drinks[drinks.continent=="Africa"].beer_servings.mean()}')

# only select the drinks by continent and show max
# print(f'{drinks.groupby("continent").beer_servings.max()}')

# only select the drinks by continent and show min
# print(f'{drinks.groupby("continent").beer_servings.min()}')

# only select the drinks by continent and show aggregate
print(f'{drinks.groupby("continent").beer_servings.agg(["count", "min", "max", "mean"])}')

# You don't have to specify the column for mean
print(f'{drinks.groupby("continent").mean()}')
