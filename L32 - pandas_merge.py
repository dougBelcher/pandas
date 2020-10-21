# L32 - Joining (merging) DataFrames
# https://www.youtube.com/watch?v=iYWKfUOtGaw&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=32

import pandas as pd

# Movie items (u.item)
movie_cols = ['movie_id', 'title']
movies = pd.read_table('http://bit.ly/movieitems', sep='|', header=None, names=movie_cols, usecols=[0, 1])

# Movie ratings data (u.data)
rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('http://bit.ly/movielensdata', sep='\t', header=None, names=rating_cols)


# print(f'{movies.columns}')
# print(f'{movies.head()}')
# print(f'{movies.shape}')

# print(f'{ratings.head()}')
# print(f'{ratings.shape}')
# print(f'{ratings.loc[ratings.movie_id == 1, :].head()}')
# print(f'{ratings.movie_id.nunique()}')
# print(f'{ratings.loc[ratings.movie_id== 1, :].head()}')

movie_ratings = pd.merge(movies, ratings)
print(f'{movie_ratings.columns}')
print(f'{movie_ratings.head()}')
