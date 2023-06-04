"""
Purpose: Regular Expressions

patterns
    *  previous character can occur 0 or more times
    +  previous character can occur 1 or more times
    ?  previous character can occur 0 or 1 time only

? is generally used to make the pattern non-greedy
"""
import re

# NON- Greedy patterns
print(re.match("ab", "ab").group())
print(re.search("ab", "ab").group())
print()

print(re.search("ab?", "a").group())  # b is occurring 0 times
print(re.search("ab?", "ab").group())  # b is occurring 1 times
print(re.search("ab?", "abb").group())  # b is occurring 2 times
print(re.search("ab?", "abbbbbb").group())  # b is occurring 6 times
print(re.search("ab?", "abbbbbbbbbbbbbbbbbbbbbbbbbb").group())

# print(re.search('ab?', 'bbbbbb').group())  # b is occurring 6 times
print(re.search("a?b?", "bbbbbb").group())  # b is occurring 6 times; a - 0 times
print()

# .? Any character( except newline) can occur  0 or 1 time only
print(re.search("a.?", "a").group())  # b is occurring 0 times
print(re.search("a.?", "ab").group())  # b is occurring 1 times
print(re.search("a.?", "abb").group())  # b is occurring 2 times
print(re.search("a.?", "abbb").group())  # b is occurring 3 times

print(re.search("a.?", "a").group())
print(re.search("a.?", "ar").group())  # r is occurring 1 times
print(re.search("a.?", "amm").group())
print(re.search("a.?", "ank").group())

# print(re.search('a.?', 'bbbbbbb').group())     # a is occurring 0 times
print(re.search("a?.?", "bbbbbbb").group())  # a is occurring 0 times
