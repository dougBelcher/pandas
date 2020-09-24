# Why do some pandas commands end with parens and others don't
# https://www.youtube.com/watch?v=hSrDViyKWVk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=4
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html

import pandas as pd

pd.set_option("display.max_columns", 20)

movie_columns = ['star_rating', 'title', 'content_rating', 'genre', 'duration', 'actors_list']
movies = pd.read_csv('http://bit.ly/imdbratings', names=movie_columns, header=None, index_col=None)
# print(f'{movies.head()}')             # methods - action
# print(f'{movies.describe()}')         # methods - action
print(f'{movies.shape}')                # attributes - who you are
print(f'{movies.dtypes}')               # attributes - who you are
print(f'{type(movies)}')
print(f'{movies.describe(include=["object"])}')
