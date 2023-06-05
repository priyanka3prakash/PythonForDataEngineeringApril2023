"""
Purpose: Constructor with args
"""


# class definition
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + " walks.")


if __name__ == "__main__":
    # Instantiation

    # Animal()
    # TypeError: Animal.__init__() missing 1 required positional argument: 'name'

    duck = Animal("Duck")
    # Animal.__init__(duck, "Duck")

    print(duck)

    # TO retrieve the instance variables
    print(vars(duck))
    print(f"duck.name:{duck.name}")

    # calling instance method
    duck.walk()

    # -------------------
    rhino = Animal("African Rhino")
    rhino.walk()

    # TO retrieve the instance variables
    print(vars(rhino))
    print(f"rhino.name:{rhino.name}")
