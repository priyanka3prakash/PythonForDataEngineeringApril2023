#!/usr/bin/python3
"""
Purpose: Using Custom Exception
"""
# # Method 1 - stop when exception is raised
# try:
#     votes = 0
#     i = 0
#     while i < 5:
#         age = int(input("Enter the age:"))
#         if age <= 0:
#             raise Exception('Invalid Entry for the age!')
#         elif age < 18:
#             raise Exception('You are Ineligible to vote!!')
#         else:
#             votes += 1
#         i += 1
# except Exception as ex:
#     print(f'{ex=}')
# else:
#     print(f"Total Eligible Voters: {votes}")


# Method 2 - stop when exception is raised
# votes = 0
# i = 0
# while i < 5:
#     try:
#         age = int(input("Enter the age:"))
#         if age <= 0:
#             raise Exception('Invalid Entry for the age!')
#         elif age < 18:
#             raise Exception('You are Ineligible to vote!!')
#         else:
#             votes += 1
#     except Exception as ex:
#         print(f'{ex=}')
#     else:
#         i += 1
# else:
#     print(f"Total Eligible Voters: {votes}")


# Method 3 - skip the loop with exception
class InvalidInput(Exception):
    pass


class InvalidAge(Exception):
    pass


votes = 0
i = 0
while i < 5:
    try:
        age = int(input("Enter the age:"))
        if age <= 0:
            raise InvalidInput("Invalid Entry for the age!")
        elif age < 18:
            # raise InvalidAge('You are Ineligible to vote!!')
            raise InvalidAge(f"You are short by {18 - age} years for voting")
        else:
            votes += 1
    except Exception as ex:
        print(f"{ex=}")
    else:
        i += 1
