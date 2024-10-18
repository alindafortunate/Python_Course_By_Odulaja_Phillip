#  A basic program that return the sam of two numbers.


def add_numbers(a, b):
    result = a + b

    print("I am a string inside the function.")
    return result
    print(
        "I am s tring after the return function."
    )  # This can't be executed because the code exits upon reaching a return statement


sum_result = add_numbers(3, 5)
print(sum_result)
# return sum_result #This too can't be executed because the return statement only works inside the function.
