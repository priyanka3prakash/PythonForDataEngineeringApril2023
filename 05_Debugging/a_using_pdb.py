#!/usr/bin/python3
"""
Purpose: Debugging
"""
val_1 = int(input("Enter val_1      :"))
val_2 = int(input("Enter val_2      :"))

import pdb; pdb.set_trace()

# Multiplication
result =  val_1 * val_2  #  val_1 + val_2
print(f"Multiplication   :{result}")

# NOTE: ;(semi-colon) is statement separator
