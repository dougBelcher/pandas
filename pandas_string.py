# How do I use string methods in pandas

import pandas as pd


# Rtv Chipotle orders table
orders = pd.read_table('http://bit.ly/chiporders')

# Convert the Item Name to Upper Case
# print(f'{orders.item_name.str.upper()}')

# Only display rows have Chicken in the Item Name
# print(f'{orders[orders.item_name.str.contains("Chicken")]}')

# Replace the left bracket ([) with a Null
# print(f'{orders.choice_description.str.replace("[", "").str.replace("]", "")}')
# orders = orders.choice_description.str.replace("\[\]", ""), inplace=True       This does not work, yet!

# print(f'{orders.choice_description}')
