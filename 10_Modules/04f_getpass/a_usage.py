import getpass

# print(dir(getpass))

# user_name = input("Enter user name:")
user_name = getpass.getuser()

# pass_word = input('Enter password :')
pass_word = getpass.getpass("Enter password :")

print(
    f"""
    Entered Details
        {user_name =}
        {pass_word =}
"""
)
