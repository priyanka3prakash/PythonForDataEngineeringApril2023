"""
In [1]: import re

In [2]: re.search("My", "My name is Ethan")
Out[2]: <re.Match object; span=(0, 2), match='My'>

In [3]: re.search("My", "My name is Mythili")
Out[3]: <re.Match object; span=(0, 2), match='My'>

In [4]: re.findall("My", "My name is Mythili")
Out[4]: ['My', 'My']

In [5]: re.findall("\bMy\b", "My name is Mythili")
Out[5]: []

In [6]: re.findall(r"\bMy\b", "My name is Mythili")
Out[6]: ['My']

In [7]: re.findall(r"\bMy", "My name is Mythili")
Out[7]: ['My', 'My']

In [8]:

In [8]: re.findall(r"\BMy\B", "My name is Mythili")
Out[8]: []

In [9]: re.findall(r"My\B", "My name is Mythili")
Out[9]: ['My']

In [10]: re.findall(r"\\", "x\\y")
Out[10]: ['\\']

In [11]: re.findall(r"\\", r"x\\y")
Out[11]: ['\\', '\\']

In [12]: re.findall("\\", r"x\\y") # error: bad escape (end of pattern) at position 0

In [13]: re.findall("\\\\", r"x\\y")
Out[13]: ['\\', '\\']


"""
