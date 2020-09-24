# How do I explore a pandas Series?
# https://www.youtube.com/watch?v=QTVTq8SPzxM&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=15
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

# print(f'{pd.get_option("display.max_columns")}')
pd.set_option("display.max_columns", 20)
# print(f'{pd.get_option("display.max_columns")}')

# print(f'{pd.option}')
# print(f'{movies.genre.describe()}')

# print(f'{movies.genre.value_counts()}')

# Use normalize to print percentages
# print(f'{movies.genre.value_counts(normalize=True)}')

# what are all the unique values in this series
# print(f'{movies.genre.unique()}')
# print(f'{movies.genre.nunique()}')

# Cross tab
# print(f'{pd.crosstab(movies.genre, movies.content_rating)}')

# mean
print(f'{movies.duration.describe}')
print(f'{movies.duration.mean()}')
