"""
Purpose: Imutable values
"""
import logging 
logging.basicConfig(level=logging.DEBUG)

class MyClass:
    def __init__(self, getter_func):
        logging.debug("In __init__ method")
        self.getter_func = getter_func
        self.setter_func = None

    def __get__(self, obj, cls):
        logging.debug("In __get__ method")
        return self.getter_func(obj)

    def setter(self, setter_func):
        logging.debug("In setter method")
        self.setter_func = setter_func

    def __set__(self, obj, value):
        logging.debug("In __set__ method")
        if self.setter_func is None:
            raise RuntimeError("This attribute cannot be set!")

        self.setter_func(obj, value)

def hello():
    return "Hello world"

val1 = MyClass(hello)

print(f"{val1.getter_func =}")


#__get__ and __getattr__