def average_calculator(numbers):
    """
    This function calculates the average of numbers.
    """

    sum_of_numbers = 0
    for i in numbers:
        sum_of_numbers += i
    average = sum_of_numbers / len(numbers)
    return average
