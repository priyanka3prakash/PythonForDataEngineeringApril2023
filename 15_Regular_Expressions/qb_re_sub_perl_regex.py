"""
Purpose: Perl compatible regex substitution
"""

import re

text = """

hello  hello
goodbye
bye   bye bye
hello goodbye
"""

# To remove duplicate words, linewise
pat = re.compile(r"(?P<word>\S*) (\s+(?P=word))", re.MULTILINE)
print(pat.findall(text))
print(pat.search(text).group())

result = pat.sub(r"\g<word>", text)
print(result)
