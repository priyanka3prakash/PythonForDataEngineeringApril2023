#!/usr/bin/python3
"""
Purpose: Exception Hooks
    - When exception is raised with excepthook set,
        case 1: when exception is handled with except block,
                it works as ordinary exception handling
        case 2: When exception is not handled with except block,
                exception hook function is executed, and program stops
"""
import sys

def my_excepthook(exc_type, exc_value, exc_traceback):
    print("\nUnhandled error")
    print(
        f"""
    exc_type     : {exc_type},
    exc_value    : {exc_value},
    exc_traceback: {exc_traceback},
        Error Line: {exc_traceback.tb_lineno},
        tb_lasti  : {exc_traceback.tb_lasti},
        tb_next   : {exc_traceback.tb_next}
        tb_frame  : {exc_traceback.tb_frame},
    """
    )

sys.excepthook = my_excepthook

print("Before exception")

# case 1
# 1 / 0

# case 2
try:
    1 / 0
except ZeroDivisionError as ex:
    print(f"{ex=}")



# case 3
raise RuntimeError("case3: This is error message")
