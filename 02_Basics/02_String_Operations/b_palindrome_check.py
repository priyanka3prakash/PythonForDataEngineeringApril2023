#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable
Step 2: Get the string reversal
Step 3: Equate and compare them

"""
test_string = input("Enter any string:")
print("test_string    =", test_string)

reverse_string = test_string[::-1]

print(test_string, reverse_string, test_string == reverse_string)

if test_string == reverse_string:
    print(test_string, "is palindrome")
else:
    print(test_string, "is not a palindrome")
