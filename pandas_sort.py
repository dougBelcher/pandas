# How do I sort a pandas dataframe or Series

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
# print(f'{movies}')

print(f'{movies.title.sort_values()}')

# movies = movies.sort_values('title', inplace=True)
# print(f'{movies}')