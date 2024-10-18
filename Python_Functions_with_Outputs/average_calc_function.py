def average_calculator(numbers):
    """
    A function that calculates the average of certain numbers.
    """
    list_of_numbers = numbers.split(", ")

    sum_of_numbers = 0
    for i in list_of_numbers:
        sum_of_numbers += int(i)
    average = sum_of_numbers / len(list_of_numbers)

    return average


print(
    average_calculator(
        input("Enter the ages you want separated by a comma and a space: ")
    )
)
