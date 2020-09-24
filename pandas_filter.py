# How Do I Filter rows of Pandas DataFrame by Column Dat

import pandas as pd

# Read the .csv from the bit.ly link
movies = pd.read_csv('http://bit.ly/imdbratings')
# print(f'{movies}')

# Create the variable booleans, iterate through the the list, and output to booleans
booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

# print(f'{booleans}')
# print(f'{len(booleans)}')

# Convert the booleans to a pandas Series and only print out rows that fit the criteria
is_long = pd.Series(booleans)
# print(f'{movies[is_long]}')

# Short way - first part replaces the for loop
is_long = movies.duration >= 200
# print(f'{movies[is_long]}')

print(f'{movies[movies.duration >= 200]}')
print(f'{movies[movies.duration >= 200].genre}')
# print(f'{movies.loc[movies.duration >= 200, 'genre']}')

