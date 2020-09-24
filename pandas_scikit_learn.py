# How do I use pandas with scikit-learn to create Kaggle submissions?

import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')

# print(f'{train.head()}')

feature_cols = ['Pcass', 'Parch']
x = train.loc[:,feature_cols]

y = train.Survived

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x,y)
