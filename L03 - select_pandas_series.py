# L03 How do I select a pandas Series from a DataFrame?
# https://www.youtube.com/watch?v=zxqjeyKP2Tk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=3

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

# print(ufo)
# print(ufo.City)                                   # with no space (sometimes work)
# print(ufo['Colors Reported'])                     # with space (always work)
ufo['Location'] = ufo.City + ', ' + ufo.State       # To create new col you have to use []
print(ufo.Location)
print(ufo.head())
