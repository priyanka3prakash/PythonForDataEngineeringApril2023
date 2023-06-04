"""
purpose: regular expression

    re.split
"""
import re

print(re.findall(".", "244.255.190.23"))
print()

print(re.findall("\.", "244.255.190.23"))
print(re.findall("[.]", "244.255.190.23"))
print()

print(re.split("\.", "244.255.190.23"))
print(re.split("[.]", "244.255.190.23"))
print()

print(re.split("[.]", "244.255.190.23", 0)) #default. all splits
print(re.split("[.]", "244.255.190.23", 1))  # ['244', '255.190.23']
print(re.split("[.]", "244.255.190.23", 2))  # ['244', '255', '190.23']
print(re.split("[.]", "244.255.190.23", 3))  # ['244', '255', '190', '23']
print(re.split("[.]", "244.255.190.23", 4))  # ['244', '255', '190', '23']
print(re.split("[.]", "244.255.190.23", 5))  # ['244', '255', '190', '23']
