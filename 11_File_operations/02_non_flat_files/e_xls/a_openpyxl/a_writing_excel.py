"""
Purpose: tO create excel file 

    pip install openpyxl --user
"""

import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "Hello"
sheet["A2"] = 213
sheet["A3"] = 123.123
sheet["B3"] = None
sheet["B4"] = True
sheet["B5"] = str((1, 2, 3))
sheet["B6"] = str([1, 2, 3])
sheet["C1"] = str({"a": 1})
workbook.save("first.xlsx")