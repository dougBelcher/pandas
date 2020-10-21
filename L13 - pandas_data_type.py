# L13 - How do I change the data type of a pandas Series?
# https://www.youtube.com/watch?v=V0AWyzVMf54&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=13

import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

# print(f'{drinks.head()}')
# print(f'{drinks.dtypes}')

# drinks['beer_servings'] = drinks.beer_servings.astype(float)          # Series method
# print(f'{drinks.head()}')
# print(f'{drinks.dtypes}')

# drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings': float})
# print(f'{drinks.dtypes}')

orders = pd.read_table('http://bit.ly/chiporders')
print(f'{orders.item_price.str.replace("$", "").astype(float).mean()}')
