# L19 - How do I select a pandas Series from a dataframe
# https://www.youtube.com/watch?v=xvpNA7bC8cs&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=19

import pandas as pd

ufo_columns = ['City', 'Colors Reported', 'Shape Reported', 'State', 'Time']
ufo = pd.read_table('http://bit.ly/uforeports', header=None, sep=',')
print(f"{ufo}")
