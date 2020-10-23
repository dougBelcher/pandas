# Why do some pandas commands end with parentheses, and other commands don't?
# https://www.youtube.com/watch?v=hSrDViyKWVk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=4

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

# print(movies.head())
# print(movies.describe())
print(movies.shape)
print(movies.dtypes)
