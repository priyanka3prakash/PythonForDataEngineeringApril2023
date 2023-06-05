#!/usr/bin/python
"""
Purpose: Debugging

TASK - To display all even numbers between 0 & 100

NOTE:
    ;(semi-colon) is statement separator
    breakpoint()
        - builtin function, introducted in python 3.6
        - same as import pdb; pdb.set_trace()
"""
numbers = range(0, 100 + 1)

# import pdb; pdb.set_trace()
breakpoint()

# To display all even numbers
for each_num in numbers:
    if each_num % 2 == 0:  # each_num % 2
        print(each_num)

# Post Analysis

# python -i SCRIPTNAME.py

#               id
#  break 21  -- 1
# break 20   --- 2
#  break 13 -- 3
#  break 19  --- 4
