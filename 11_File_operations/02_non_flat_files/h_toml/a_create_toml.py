#!/usr/bin/python3
"""
Purpose: TOML - Tom's Obvious, Minimal Language.


    https://toml.io/en/
    https://github.com/toml-lang/toml

pip install toml

"""

import toml
from pprint import pp 
# print(dir(toml))
# print()


with open("sample.toml", "r") as fh:
    parsed_toml_dict = toml.load(fh)
    
# print(parsed_toml_dict)

pp(parsed_toml_dict)
