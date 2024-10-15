# Declaring a python function.
def greeting():
    """
    This is a function that has a greeting message.
    It doesn't take in any parameter therefore it doesn't return any values.
    """

    name = input("Enter your name: ")

    message = f"Hello {name}, welcome to my first python function."

    print(message)


# Note that, without calling the function, the block of code inside can never be executed.
# greeting()  # Here I am calling the function for the first time.
# greeting()  # Here I am calling the function the second time.
# greeting()  # Here I am calling the function the third time.
