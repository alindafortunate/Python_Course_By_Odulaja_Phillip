# passing a lambda function inside another function.
def operation(operation, a, b):
    return operation(a, b)


multiply = lambda x, y: x * y
print(operation(multiply, 3, 5))

