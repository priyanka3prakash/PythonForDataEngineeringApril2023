#!/usr/bin/python3
"""
Purpose: TOML - Tom's Obvious, Minimal Language.


    https://toml.io/en/
    https://github.com/toml-lang/toml

pip install toml

"""

from pprint import pp

import toml

# print(dir(toml))
# print()


with open("sample.toml") as fh:
    parsed_toml_dict = toml.load(fh)

# print(parsed_toml_dict)

pp(parsed_toml_dict)
