"""
Purpose: Usage of Dunder (magic or Double underscore) methods

"""


class RationalNumber:
    """
    Rational Numbers with support for arithmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
    """

    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d - self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    __repr__ = __str__


a = RationalNumber(1, 2)  # a.n = 1,a.d=2
b = RationalNumber(2)
c = 29

print(isinstance(a, RationalNumber))  # True
print(isinstance(b, RationalNumber))  # True
print(isinstance(c, RationalNumber))  # False
print(isinstance(c, int))  # True
print()


print(a.__add__(b))
print(a + b)  # same as a.__add__(b)

print(a.__add__(c))
print(a + c)  # same as a.__add__(c)
print()


print(a.__sub__(b))
print(a - b)  # same as a.__sub__(b)
print()

print(a.__str__())
print(str(a))  # same as a.__str__()

print(a.__repr__())
print(repr(a))


# === Another Example
class Student:
    def __init__(self, id, marks):
        self.id = id
        self.__marks = marks

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def __add__(self, other):
        print(other.get_marks() - self.get_marks())


comb = Student(1, 90) + Student(2, 40)
print("comb", comb)
