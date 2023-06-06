# Example 2: String reversal
"""
Python  # take first char and place at end
ythonP
thonPy
honPyt
onPyth
nPytho
nohtyP
"""


def string_reversal(word):
    if len(word) == 0:
        return ""
    print(word)
    return string_reversal(word[1:]) + word[0]


print(string_reversal("Python"))


# Python  # take last char and place at start
"""
nPytho
onPyth
honPyt
thonPy
....
"""


def string_reversal_1(word):
    if not word:
        return ""
    print(f"{word =}")
    return word[-1] + string_reversal_1(word[:-1])


result = string_reversal_1("Python")
print(result)
