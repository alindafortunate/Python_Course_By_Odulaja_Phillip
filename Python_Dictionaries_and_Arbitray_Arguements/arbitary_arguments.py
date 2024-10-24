# A program to demonstrate the working of arbitary arguments.


def my_function(*args):
    for arg in args:
        print(arg)


my_function("first_name", "gender", "education")


# Instead of *args, you can use any approved variable name like *parameters.
def my_function(*parameters):
    for parameter in parameters:
        print(parameter)
    print(parameters)


my_function("first_name", "gender", "education")
