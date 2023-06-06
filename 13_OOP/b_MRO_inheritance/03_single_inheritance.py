"""
Purpose: Single Inheritance

    int

    Myint
"""


class MyInt(int):
    pass


m = MyInt()
print(MyInt.__mro__)
# (<class '__main__.MyInt'>, <class 'int'>, <class 'object'>)
