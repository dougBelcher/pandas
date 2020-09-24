# How do I apply Multiple Filter Criteria to a pandas DataFrame

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

# print(f'{movies}')
# print(f'{movies[(movies.duration >= 200)]}')
# print(f'{movies[(movies.duration >= 200) & (movies.duration <= 220)]}')
# print(f'{movies[(movies.duration >= 200) & (movies.genre == "Drama")]}')
print(f'{movies[movies.genre.isin(["Crime", "Action", "Drama"])]}')
