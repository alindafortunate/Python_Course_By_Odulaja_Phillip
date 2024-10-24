# A program to demonstrate how python **kwargs operate.


def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

    print(kwargs)


my_function(fruit="apple", animal="cow", insect="bee")
