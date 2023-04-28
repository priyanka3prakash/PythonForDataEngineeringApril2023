#!/usr/bin/python
""""
Purpose: calculator
"""



try:
    num1  = float(input("num1 ="))
    num2  = float(input("num2 = "))

    add_res = num1 + num2
    sub_res = num1 - num2
    mul_res = num1 * num2

    div_res = num1 /num2
except ZeroDivisionError as ex:
    print(ex)
    print("Ensure num2 is non Zero")
except ValueError as ve:
    print(ve)
except Exception as ex:
    print("Unhandled exception:", repr(ex))
else:
    print(f""" 
        addition        : {add_res}
        subtraction     : {sub_res}
        multiplication  : {mul_res}
        division        : {div_res}
    """)
finally:
    print("FInally Block")

print("next statement")