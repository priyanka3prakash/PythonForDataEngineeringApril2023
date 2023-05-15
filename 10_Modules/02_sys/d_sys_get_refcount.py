#!/usr/bin/python3
"""
Purpose: sys module
"""
import sys

print(f"{sys.getrefcount(123) =}")


num1 = 123
num2 = 123
num3 = 123
print(f"{sys.getrefcount(123) =}")
# NOTE: Returns how many variables are referring to this value
# Every number will have atleast 2 references


for i in range(800):
    print(f"{i} {sys.getrefcount(i)}")
print()


print(f"{sys.getrefcount(-0.2) =}")
print(f"{sys.getrefcount(None) =}")
print(f"{sys.getrefcount(1)    =}")
print(f"{sys.getrefcount(True) =}")
print(f"{sys.getrefcount(0)    =}")
print(f"{sys.getrefcount(False)=}")

name = "Neha Rehman"
print(f'{sys.getrefcount("Neha Rehman")=}')  # 4

mylist = [45, 87, 23]
print(f"{sys.getrefcount([45, 87, 23])=}")
print()

a = {"hello": 42, "world": 99}
b = a

print("\nMoving on to some introspection of the object heap.")
# This is 3 instead of 2, because the getrefcount function has a local
# parameter variable pointing to the object received by the function.
print(f"The dictionary is referred to by {sys.getrefcount(a)} references.")
print(f"The dictionary size is {sys.getsizeof(a)} bytes.")
