#!/usr/bin/python3
"""
Purpose: sys.path
    - Gives the paths to refer
    Scope Resolution - LEGB
        - Builtin

"""

import sys

# print(sys.path) # gives a list of paths

for each_path in sys.path:
    print(each_path)

# /workspaces/PythonForDataEngineeringApril2023/10_Modules/02_sys
# /usr/local/python/3.10.4/lib/python310.zip
# /usr/local/python/3.10.4/lib/python3.10
# /usr/local/python/3.10.4/lib/python3.10/lib-dynload
# /home/codespace/.local/lib/python3.10/site-packages
# /usr/local/python/3.10.4/lib/python3.10/site-packages


# NOTE: Installed modules are stored in "site-packages"


# def add(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# print(f"{add(2, 3) =}")
# print(f"{sub(2, 3) =}")

# Case 1 - importing script from current directory
import j_calculator

print(dir(j_calculator))

print(f"{j_calculator.add(2, 3) =}")
print(f"{j_calculator.sub(2, 3) =}")


# Case 1.1 - selective import
from j_calculator import add

assert j_calculator.add(2, 3) == add(2, 3)


# sub(2,3)  # NameError: name 'sub' is not defined. Did you mean: 'sum'?
print()

# Case 2
from myfolder import myops

print(dir(myops))

print(f"{myops.math.sqrt(81) =}")
print(f"{myops.factorial(8) =}")

# Case 2.1
from myfolder.myops import factorial

print(f"{factorial(8) =}")


sys.dont_write_bytecode = True
# pycache files are not created when it is True


# case 3 - - script present in different directory
# from ../../06_Collections/04_Dicts import fib

# sys.path.append("../../06_Collections/04_Dicts")
sys.path.insert(0, "../../06_Collections/04_Dicts")

for each_path in sys.path:
    print(each_path)


import fib

print(dir(fib))

print(f"{fib.DOZEN = }")
print(f"{fib.fibonacci_series(4) = }")
