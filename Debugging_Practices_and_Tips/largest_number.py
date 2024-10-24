# A program to find the largest number in a python list.
from typing import List


def find_largest_number(numbers: List):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


numbers = [17, 19, 20, 7]
print(find_largest_number(numbers))
