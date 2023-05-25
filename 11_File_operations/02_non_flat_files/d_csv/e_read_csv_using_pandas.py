#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv using pandas module
    pip install -U pandas --user
"""

import pandas  as pd

# print(dir(pd))

data_frame = pd.read_csv("first.csv")

print(type(data_frame))
print(data_frame)
print()

print(data_frame.head())
print()

# data_frame.name
names = list(data_frame["name"])
print(f"{names = }")
