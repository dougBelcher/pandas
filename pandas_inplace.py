# When should I use the "inplace" parameter in pandas?

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(f'{ufo.columns}')

ufo.drop("City", axis=1, inplace=True)
print(f'{ufo}')
