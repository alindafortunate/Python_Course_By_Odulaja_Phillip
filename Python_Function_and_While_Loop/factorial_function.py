# A program to return the factorial of any positive integer.


def factorial(number):

    result = 1

    if number == 0:
        print(1)
    else:
        while number > 1:

            result *= number

            number -= 1

        print(result)


factorial(3)
