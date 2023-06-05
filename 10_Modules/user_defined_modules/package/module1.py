import sys


def hello_world():
    print("Hello from Module1")


if __name__ == "__main__":
    hello_world()
else:
    print(
        f"""
        {__name__    =}
        {__package__ =}
    """
    )
