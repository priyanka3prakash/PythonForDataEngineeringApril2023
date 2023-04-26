#!/usr/bin/python3
"""
Purpose: Number Guessing Game

    break - To come out of any loop (for/while)
"""
LUCKY_NUMBER = 67

# Method 1 - No limit on number of chances(attempt)
# given_number = int(input('Enter no. between 0 & 100:'))

# if given_number == LUCKY_NUMBER:
#     print('You guessed correctly!')
# elif given_number > LUCKY_NUMBER:  # 87 > 67
#     print('Reduce your guessing number')
# else:  # given_number < LUCKY_NUMBER
#     print('Increase your guessing number')


# # Method 2 - To limit the number of attempts
# attempt = 0
# while attempt < 5:
#     attempt += 1

#     given_number = int(input('Enter no. between 0 & 100:'))

#     if given_number == LUCKY_NUMBER:
#         print('You guessed correctly!')
#     elif given_number > LUCKY_NUMBER:  # 87 > 67
#         print('Reduce your guessing number')
#     else:  # given_number < LUCKY_NUMBER
#         print('Increase your guessing number')

#     if attempt == 5:
#         print(f'Sorry! YOu failed to guess in all {attempt} attempts'.upper())

# # Method 3 - while with else condition
attempt = 0
while attempt < 5:
    attempt += 1

    given_number = int(input('Enter no. between 0 & 100:'))

    if given_number == LUCKY_NUMBER:
        print('You guessed correctly!')
    elif given_number > LUCKY_NUMBER:  # 87 > 67
        print('Reduce your guessing number')
    else:  # given_number < LUCKY_NUMBER
        print('Increase your guessing number')
else:
    print(f'Sorry! YOu failed to guess in all {attempt} attempts'.upper())
