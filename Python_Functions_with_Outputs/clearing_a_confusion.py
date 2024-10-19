# Please do not focus on this program,
# It was for my own personal benefit.


def average(numbers):
    list_of_numbers = numbers.split(", ")
    sum_of_numbers = 0
    count = 0
    for num in list_of_numbers:
        sum_of_numbers += int(num)
        count += 1
    print(count)
    average = sum_of_numbers / count
    return average


# Hahahaha, actually in that for loop the num is just a variable to hold,
# the items of numbers as you iterate through them.
# So in the ideal sense num is a string, because after being splitted, the are left with a string data type.
# That is why, we have to convert them to an int to add them to sum_of_numbers.
# May your name be gloried always.

my_numbers = input("Enter numbers separated by a comma and a space e.g 1, 2, 3: ")
print(average(my_numbers))
