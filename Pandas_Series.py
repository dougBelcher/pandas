# How do I select a pandas Series from a dataframe

import pandas as pd

ufo_columns = ['City', 'Colors Reported', 'Shape Reported', 'State', 'Time']
ufo = pd.read_table('http://bit.ly/uforeports', header=None, sep=',')
print(f"{ufo}")
