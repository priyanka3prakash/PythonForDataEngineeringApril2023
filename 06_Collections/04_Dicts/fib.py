DOZEN = 12


def fibonacci_series(num):
    nums = []
    num1, num2 = 0, 1
    for _ in range(num):
        num1, num2 = num2, num1 + num2
        nums.append(num2)
    return nums


if __name__ == "__main__":
    print("this script is executed directly")
    print(f"{fibonacci_series(10) = }")
    print(f"{fibonacci_series(5) = }")
    print(f"{fibonacci_series(1) = }")
    print(f"{fibonacci_series(3) = }")
else:
    print("this script is imported")
