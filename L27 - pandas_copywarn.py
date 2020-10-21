# L27 - How do I avoid a SettingWithCoyWarning in pandas?
# https://www.youtube.com/watch?v=4R4WsDJ-KVc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=27

import pandas as pd
import numpy as np

movies = pd.read_csv('http://bit.ly/imdbratings')

# pd.set_option("display.max_columns", 5)
print(f'{pd.get_option("display.max_columns")}')

print(f'{movies.head()}')
# print(f'{movies.content_rating.isnull().sum()}')
# print(f'{movies[movies.content_rating.isnull()]}')
# print(f'{movies.content_rating.value_counts()}')
# print(f'{movies[movies.content_rating=="NOT RATED"]}')
# print(f'{movies[movies.content_rating=="NOT RATED"].content_rating}')
# movies[movies.content_rating == 'NOT RATED'].content_rating = np.nan          # throws warning
# movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan     # no warning
# print(f'{movies.content_rating.isnull().sum()}')

# top_movies = movies.loc[movies.star_rating >= 9, :]           # throws warning
top_movies = movies.loc[movies.star_rating >= 9, :].copy()      # no warning
print(f'{top_movies.duration}')
top_movies.loc[0, 'duration'] = 150
print(f'{top_movies.duration}')
