# A program to apply the divide and conquer technique in solving bugs in the code.
from typing import List


# ------------PART 1---------------PASSED.
def calculate_average(numbers: List):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average


# print(calculate_average([1, 2, 3]))


# -------------PART 2------------PASSED
def find_largest(numbers: List):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


# print(find_largest([1, 4, 5, 6, 2]))


# -----------PART 3-------------PASSED
def main():
    numbers = input("Enter a list of numbers, separated by a comma: ")
    tokenize_numbers = numbers.split(",")
    int_numbers = []
    for number in tokenize_numbers:
        int_numbers.append(int(number))
    average = calculate_average(int_numbers)
    largest = find_largest(int_numbers)

    print(f"Average is: {average}")
    print(f"Largest number is: {largest}")


main()
