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

In [12]: re.findall("\\", r"x\\y")
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
Cell In[12], line 1
----> 1 re.findall("\\", r"x\\y")

File C:\Python311\Lib\re\__init__.py:216, in findall(pattern, string, flags)
    208 def findall(pattern, string, flags=0):
    209     """Return a list of all non-overlapping matches in the string.
    210
    211     If one or more capturing groups are present in the pattern, return
   (...)
    214
    215     Empty matches are included in the result."""
--> 216     return _compile(pattern, flags).findall(string)

File C:\Python311\Lib\re\__init__.py:294, in _compile(pattern, flags)
    288     import warnings
    289     warnings.warn("The re.TEMPLATE/re.T flag is deprecated "
    290               "as it is an undocumented flag "
    291               "without an obvious purpose. "
    292               "Don't use it.",
    293               DeprecationWarning)
--> 294 p = _compiler.compile(pattern, flags)
    295 if not (flags & DEBUG):
    296     if len(_cache) >= _MAXCACHE:
    297         # Drop the oldest item

File C:\Python311\Lib\re\_compiler.py:743, in compile(p, flags)
    741 if isstring(p):
    742     pattern = p
--> 743     p = _parser.parse(p, flags)
    744 else:
    745     pattern = None

File C:\Python311\Lib\re\_parser.py:973, in parse(str, flags, state)
    970 def parse(str, flags=0, state=None):
    971     # parse 're' pattern into list of (opcode, argument) tuples
--> 973     source = Tokenizer(str)
    975     if state is None:
    976         state = State()

File C:\Python311\Lib\re\_parser.py:230, in Tokenizer.__init__(self, string)
    228 self.index = 0
    229 self.next = None
--> 230 self.__next()

File C:\Python311\Lib\re\_parser.py:243, in Tokenizer.__next(self)
    241         char += self.decoded_string[index]
    242     except IndexError:
--> 243         raise error("bad escape (end of pattern)",
    244                     self.string, len(self.string) - 1) from None
    245 self.index = index + 1
    246 self.next = char

error: bad escape (end of pattern) at position 0

In [13]: re.findall("\\\\", r"x\\y")
Out[13]: ['\\', '\\']


"""