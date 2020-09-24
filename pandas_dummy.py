# How do I crete dummy variables in pandas
# https://www.youtube.com/watch?v=0s_1IsROgDc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=24

import pandas as pd

pd.set_option("display.max_columns", 20)

train = pd.read_csv('http://bit.ly/kaggletrain')

# Passing Series
# train['Sex_male'] = train.Sex.map({'female': 0, 'male': 1})

# print(f'{train.head()}')

# print(f'{pd.get_dummies(train.Sex, prefix="Sex").head().iloc[:, 1:]}')

# print(f'{train.Embarked.value_counts}')
# print(f'{pd.get_dummies(train.Embarked, prefix="Emb")}')
# print(f'{pd.get_dummies(train.Embarked, prefix="Emb").iloc[:, 1:]}')
# emb_dummies = pd.get_dummies(train.Embarked, prefix='Emb').iloc[:, 1:]
# train = pd.concat([train, emb_dummies], axis=1)
# print(f'{train.head()}')

# Pass dataFrame
# print(f'{}')
print(f'{pd.get_dummies(train, columns=["Sex", "Embarked"])}')
