
# A program for calculating the simple interest rate.

# Declaring the function with three parameters.
def simple_interest_rate(principal, rate, time):
    """
    A function for calculating the simple interest rate.
    """
    interest = principal*(rate/100)*time

    print(f'The interest is {interest}')

# Calling the function by supplying it with three arguements
simple_interest_rate(7000, 5, 3) 