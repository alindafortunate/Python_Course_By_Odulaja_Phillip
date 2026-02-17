# A program to demonstarte raising errors.
def square_root(number):
    if number < 0:
        raise ValueError("Cannot get a squareroot of a negative number.")
    else:
        return number**0.5


print(square_root(9))
print(square_root(-1))
