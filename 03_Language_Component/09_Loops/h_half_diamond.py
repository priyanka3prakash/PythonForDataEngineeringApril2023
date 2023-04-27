#!/usr/bin/python3
"""
Purpose: To display the asterisk's in a half-diamond pattern
"""
# half-diamond
for num in range(0, 10, 1):
    print(num, num * "*")  # string repetition operator

for num in range(10, 0, -1):
    print(num, num * "*")

for num in range(0, 10, 1):
    print(num, (9 - num) * " " + num * "*")

for num in range(10, 0, -1):
    print(num, (9 - num) * " " + num * "*")

print()
# using while loop
i = 0
while i < 10:
    print(i, i * "*")
    i += 1

i = 10
while i > 0:
    print(i, i * "*")
    i -= 1

j = 0 
while j < 10:
    print(j, (9-j) * " " + j * "*")
    j += 1

j = 10
while j > 0:
    print(j, (9-j) * " " + j * "*")
    j -= 1






"""
Assignment:full diamond problem
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
 *************
  ***********
    *******
     *****
      ***
       *
"""