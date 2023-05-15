#!/usr/bin/python3
"""
Purpose: Getting Command-line arguments
"""
import sys
print(f"{__file__ =}")
print(f"{sys.argv =}")

assert __file__ != sys.argv[0]

"""
$ python k_command_line_args.py 
    __file__ ='/workspaces/PythonForDataEngineeringApril2023/10_Modules/02_sys/k_command_line_args.py'
    sys.argv =['k_command_line_args.py']

$ python ../02_sys/k_command_line_args.py 
    __file__ ='/workspaces/PythonForDataEngineeringApril2023/10_Modules/02_sys/../02_sys/k_command_line_args.py'
    sys.argv =['../02_sys/k_command_line_args.py']

$ python ../../10_Modules/02_sys/k_command_line_args.py 
    __file__ ='/workspaces/PythonForDataEngineeringApril2023/10_Modules/02_sys/../../10_Modules/02_sys/k_command_line_args.py'
    sys.argv =['../../10_Modules/02_sys/k_command_line_args.py']

$ python ../../../PythonForDataEngineeringApril2023/10_Modules/02_sys/k_command_line_args.py 
    __file__ ='/workspaces/PythonForDataEngineeringApril2023/10_Modules/02_sys/../../../PythonForDataEngineeringApril2023/10_Modules/02_sys/k_command_line_args.py'
    sys.argv =['../../../PythonForDataEngineeringApril2023/10_Modules/02_sys/k_command_line_args.py']

$ python k_command_line_args.py 12 32 234 234
    __file__ ='/workspaces/PythonForDataEngineeringApril2023/10_Modules/02_sys/k_command_line_args.py'
    sys.argv =['k_command_line_args.py', '12', '32', '234', '234']

$ python k_command_line_args.py  True None sad 2312
    __file__ ='/workspaces/PythonForDataEngineeringApril2023/10_Modules/02_sys/k_command_line_args.py'
    sys.argv =['k_command_line_args.py', 'True', 'None', 'sad', '2312']
"""


print("Number of arguments:", len(sys.argv), "arguments")
print("Arguments List:", list(sys.argv))