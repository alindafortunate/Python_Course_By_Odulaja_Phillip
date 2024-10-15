# A recap of my previous knowledge about python functions.
def greetings():
    """This functions displays a greeting message and takes in no parameters.
    It doesn't return value.
    """

    name = input("Enter your name: ")
    message = "Hello " + name + "! Welcome to the program"

    print(message)


greetings()

# Printing the docString (This is a multiline comment)
print(greetings.__doc__)
