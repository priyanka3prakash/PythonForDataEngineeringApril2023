#!/usr/bin/python3
"""
Purpose: sys module
"""
import sys
from pprint import pprint


print(
    f"""
    {sys.audit                      =}
    {sys.displayhook                =}
    {sys.int_info                   =}
    {sys.intern                     =}
    {sys.thread_info                =}
    {sys.warnoptions                =}

    {sys.builtin_module_names       =}
"""
)