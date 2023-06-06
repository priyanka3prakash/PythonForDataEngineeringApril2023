"""
Purpose: Regular Expressions

Question: How to get specific no. of characters from target string

pattern
    ^   To make to check at the start of string
    $   To make to check at the end of string
    .   To get any character, except the newline(\n) character
"""
import re

# To get 5 characters, ( default is from start of string)
result = re.search(".....", "PyTHOn Programming is good", re.I)
if result:
    print(f"result.group():{result.group()}")


# To get 5 characters, from start of string
result = re.search("^.....", "PyTHOn Programming is good", re.I)
if result:
    print(f"result.group():{result.group()}")


# To get 5 characters, from end of string
result = re.search(".....$", "PyTHOn Programming is good", re.I)
if result:
    print(f"result.group():{result.group()}")


# To get the target string with 5 characters only
result = re.search("^.....$", "PyTHOn Programming is good", re.I)
print(f"result:{result}")  # None


# To get the target string with 4 characters only
result = re.search("^....$", "PyTHOn Programming is good", re.I)
print(f"result:{result}")  # None


# To get the target string with 5 characters only
result = re.search("^.....$", "udhay", re.I)
print(f"result:{result}")

# To get the target string with 5 characters only
result = re.search(r"\A.....\Z", "udhay", re.I)
print(f"result:{result}")
print()

# To get the target string with 5 characters only
result = re.search("^.....$", "udhaya", re.I)
print(f"result:{result}")  # None

# To get the target string with 5 characters only
result = re.search(r"\A.....\Z", "udhaya", re.I)
print(f"result:{result}")  # None
